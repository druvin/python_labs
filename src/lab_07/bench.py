import csv
from src.lab_04.io_txt_csv import write_csv

import timeit
import random

from src.lab_07.sorting import (
    bubble_sort,
    insertion_sort,
    selection_sort
)

from src.lab_07.search import (
    linear_search,
    binary_search,
    two_sum_brute,
    two_sum_fast
)

def bench_sorts() -> list[tuple[str, int, str, str]]:
    """Запускает бенчмарки для сортировок и собирает данные в список с кортежами"""

    random.seed(42)
    rows = []
    sizes = [1_000, 10_000, 100_000]
    for n in sizes:
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        time_s = timeit.timeit(lambda: sorted(data), number = 1)

        rows.append(("sorting", n, "sorted", f"{time_s:.6f}"))
        funcs = [("bubble_sort", bubble_sort), ("insertion_sort", insertion_sort), ("selection_sort", selection_sort)]

        for name, fc in funcs:
            if n <= 10_000:
                time = timeit.timeit(lambda: fc(data), number = 1)
                rows.append(("sorting", n, name, f"{time:.6f}"))
            else:
                rows.append(("sorting", n, name, ">60"))
    return rows

def bench_search() -> list[tuple[str, int, str, str]]:
    """Запускает бенчмарки для поиска и собирает данные в список с кортежами"""

    random.seed(42)
    rows = []
    data = [random.randint(-1_000_000, 1_000_000) for _ in range (100_000)]
    targets = [random.choice(data) for _ in range(10000)]

    time_ls = timeit.timeit(lambda: [linear_search(data, t) for t in targets], number = 1)
    rows.append(("search", 100_000, "linear_search", f"{time_ls:.6f}"))

    sorted_data = sorted(data)
    time_bs = timeit.timeit(lambda: [binary_search(sorted_data, t) for t in targets], number = 1)
    rows.append(("search", 100_000, "binary_search", f"{time_bs:.6f}"))

    for n in [1_000, 10_000]:
        data_ts = [random.randint(-1_000_000, 1_000_000) for _ in range (n)]
        a, b = random.sample(data_ts, 2)
        targ = a + b

        t_tsb = timeit.timeit(lambda: two_sum_brute(data_ts, targ), number = 1)
        rows.append(("two_sum", n, "two_sum_brute", f"{t_tsb:.6f}"))

        t_tsf = timeit.timeit(lambda: two_sum_fast(data_ts, targ), number = 1)
        rows.append(("two_sum", n, "two_sum_fast", f"{t_tsf:.6f}"))
    
    return rows

def main():
    """Собирает все полученные списки из ранее реализованых функций в CSV и выводит сводную таблицу в консоль"""
    header = ("task", "n", "impl", "seconds")
    rows = []
    rows.extend(bench_sorts())
    rows.extend(bench_search())

    write_csv(rows, "data/lab_07/bench.csv", header)

    print("Результаты бенчмарка:")
    print(f"{'Task':<12} | {'N':<8} | {'Impl':<20} | {'Seconds':<12}")
    print('-' * 60)
    for t, n, i, s in rows:
        print(f"{t:<12} | {n:<8} | {i:<20} | {s:<12}")
    
    print("Результаты сохранены в data/lab_07/bench.csv")

if __name__ == "__main__":
    main()