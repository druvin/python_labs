import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текст из файла в указанной кодировке."""
    p = Path(path)
    # Ошибки FileNotFoundError и UnicodeDecodeError не скрываем.
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает строки в CSV. Число столбцов должно быть одинаковым."""
    p = Path(path)
    rows = list(rows)

    if header is not None:
        columns = len(header)
    elif len(rows) > 0:
        columns = len(rows[0])
    else:
        columns = 0

    for r in rows:
        if len(r) != columns:
            raise ValueError("Разное количество столбцов в CSV")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

import sys
from pathlib import Path
from collections import Counter

from src.lab_03.text import normalize, tokenize
from src.lab04.io_txt_csv import read_text, write_csv

def frequencies_from_text(text: str) -> dict[str, int]:
    """Нормализует текст и считает частоты слов."""
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует: сначала по убыванию количества, потом по алфавиту."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def print_table(rows):
    """Выводит таблицу частот в консоль."""
    print(f"{'Слово':<20} {'Количество':>12}")
    print("-" * 33)
    for word, count in rows:
        print(f"{word:<20} {count:>12}")

def main():
    files = sys.argv[1:]
    if len(files) == 0:
        files = ["data/input.txt"]

    all_freq = {}
    per_file_rows = []
    total_words = 0

    for filename in files:
        try:
            text = read_text(filename)
        except FileNotFoundError:
            print("Файл не найден:", filename, file=sys.stderr)
            sys.exit(1)
        except UnicodeDecodeError:
            print("Неверная кодировка файла:", filename, file=sys.stderr)
            sys.exit(1)

        freq = frequencies_from_text(text)
        total_words += sum(freq.values())

        # Отдельные результаты для каждого TXT-файла.
        for word, count in sorted_word_counts(freq):
            per_file_rows.append((Path(filename).name, word, count))
            all_freq[word] = all_freq.get(word, 0) + count

    rows = sorted_word_counts(all_freq)

    if len(files) == 1:
        write_csv(rows, "data/report.csv", ("word", "count"))
        print("Отчёт сохранён: data/report.csv")
    else:
        write_csv(rows, "data/report_total.csv", ("word", "count"))
        write_csv(per_file_rows, "data/report_per_file.csv", ("file", "word", "count"))
        print("Отчёты сохранены: data/report_total.csv, data/report_per_file.csv")

    print("Всего слов:", total_words)
    print("Уникальных слов:", len(all_freq))
    print("Топ-5:")
    for word, count in rows[:5]:
        print(f"{word}: {count}")

    print()
    print_table(rows)

if __name__ == "__main__":
    main()