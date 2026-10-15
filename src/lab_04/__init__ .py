# Лабораторная работа №4 — TXT, CSV и отчёт по тексту

## Задача

Программа читает текст из TXT-файла, приводит слова к одному виду, считает, сколько раз встречается каждое слово, сортирует их и сохраняет результат в CSV.

Код написан по **подсказкам из README преподавателя на GitHub**: `Path.read_text()`, `Path.open()`, `csv.writer()`, `Counter()` и сортировка с `lambda`.

## Задание 1. Чтение текста и запись CSV

Файл: `io_txt_csv.py`.

`read_text()` получает путь к файлу и кодировку (по умолчанию UTF-8). Если файла нет или кодировка неверная, Python выдаёт соответствующее исключение.

`write_csv()` сохраняет таблицу с заголовком или без него, используя `newline=""`, чтобы в Windows не появлялись лишние пустые строки.

```python
"""Функции для чтения TXT и записи CSV."""

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
```

## Задание 2. Подсчёт частот и отчёт

Файл: `text_report.py`.

Сначала вызываются `normalize()` и `tokenize()` из третьей лабораторной, затем `Counter()` считает повторения слов. Сортировка выполняется по убыванию частоты, при равной частоте — по алфавиту.

```python
"""ЛР4: текстовая статистика, TXT и CSV."""

import sys
from pathlib import Path
from collections import Counter

from src.lib.text import normalize, tokenize
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
```

## Как запускать

Команды нужно вводить **из корневой папки проекта**, где лежат `src` и `data`.

**Один TXT-файл:**

```powershell
python -m src.lab04.text_report
```

Создаст файл `data/report.csv`.

**Дополнительное задание (два или больше файлов):**

```powershell
python -m src.lab04.text_report data/a.txt data/b.txt
```

Создаст `data/report_total.csv` и `data/report_per_file.csv`.

Пример входного файла `data/input.txt`:

```text
Привет, мир! Привет!!!
```

Пример вывода:

```text
Отчёт сохранён: data/report.csv
Всего слов: 3
Уникальных слов: 2
Топ-5:
привет: 2
мир: 1
```

В CSV сохраняются **все** слова, а не только топ-5.

## Проверки

- `read_text()` принимает строку пути и объект `Path`.
- `read_text()` позволяет указать, например, `encoding="cp1251"`.
- Пустой TXT создаёт CSV с заголовком, но без строк данных.
- Ошибки `FileNotFoundError` и `UnicodeDecodeError` обрабатываются в основной программе.
- `write_csv()` проверяет одинаковое количество столбцов.
- При одинаковой частоте слова идут в алфавитном порядке.
- При нескольких входных файлах формируются отдельный и общий отчёты.

## Скриншоты для сдачи

После запуска программы сделай свои скриншоты терминала и сохрани их в `images/lab04/`, например `img01.png` и `img02.png`.

Вставить изображения в этот README можно так:

```markdown
![Основной запуск](../../images/lab04/img01.png)
![Запуск нескольких файлов](../../images/lab04/img02.png)
```

Отчёт подготовлен с учётом лекций №3–6 и подсказок преподавателя из GitHub.
