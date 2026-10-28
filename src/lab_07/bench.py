import csv
from pathlib import Path
from src.lab04.io_txt_csv import write_csv

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

def bench_sorts() -> list(tuple(str, int, str, str)):
    """Запускает бенчмарки для сортировок и собирает данные в список с кортежами"""
    
    random.seed(42)
    rows = []
    sizes = [1000, 10000, 100000]
    for n in sizes:
        data = [random.randint(-1000000, 1000000) for _ in range(n)]
        time = timeit.timeit(lambda: sorted(data), number = 1)

        rows.append(("sorting", n, "sorted", f"{t:.6f}"))
        funcs = [("bubble_sort", bubble_sort), ("insertion_sort", insertion_sort), ("selection_sort", selection_sort)]

        for name, fc in funcs:
            if n <= 10000:
                time = timeit.timeit(lambda: fc(data), number = 1)
                rows.append(("sorting", n, name, f"{time:.6f}"))
            else:
                rows.append(("sorting", n, name, ">60"))
    return rows

def bench_search() -> list(tuple(str, int, str, str)):
    """Запускает бенчмарки для поиска и собирает данные в список с кортежами"""

    random.seed(42)
    rows = []
    data = [random.randint(-1000000, 1000000) for _ in range(n)]
    sizes = [100000, 10000]
def main():
    """Собирает все полученные списки из ранее реализованых функций в CSV и выводит сводную таблицу в консоль"""
    