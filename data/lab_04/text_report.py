import sys 
from pathlib import Path 
from collections import Counter

from src.lab_03.text import normalize, tokenize 
from data.lab_04.io_txt_csv import read_text, write_csv

def frequencies_from_text(text: str) -> dict[str, int]: 
    """Нормализует текст и считает частоты слов.""" 
    tokens = tokenize(normalize(text)) 
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]: 
    """Сортирует слова по частоте и алфавиту.""" 
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def print_table(rows): 
    """Выводит общую таблицу частот.""" 
    print(f"{'Слово':<20} {'Количество':>12}") 
    print("-" * 33)

    for word, count in rows:
        print(f"{word:<20} {count:>12}")

def main(): 
    data_dir = Path(__file__).resolve().parent.parent

    files = sys.argv[1:]

    if len(files) == 0:
        files = ["input.txt"]

    files = [data_dir / filename for filename in files]

    all_freq = {}
    per_file_rows = []
    total_words = 0

    for filename in files:
        try: text = read_text(filename)
        except FileNotFoundError: print("Файл не найден:", filename)
        except UnicodeDecodeError: print("Ошибка кодировки:", filename)

        freq = frequencies_from_text(text)
        total_words += sum(freq.values())

        for word, count in sorted_word_counts(freq):
            per_file_rows.append((filename.name, word, count))
            all_freq[word] = all_freq.get(word, 0) + count

    rows = sorted_word_counts(all_freq)

    if len(files) == 1:
        write_csv(rows, data_dir / "report.csv", ("word", "count"))
        print("Отчёт сохранён: data/report.csv")
    else:
        write_csv(rows, data_dir / "report_total.csv", ("word", "count"))
        write_csv(per_file_rows, data_dir / "report_per_file.csv",
                ("file", "word", "count"))
        print("Отчёты сохранены")

    print("Всего слов:", total_words)
    print("Уникальных слов:", len(all_freq))
    print("Топ-5:")

    for word, count in rows[:5]:
        print(f"{word}: {count}")

    print()
    print("Общая таблица:")
    print_table(rows)

    if len(files) > 1:
        print()
        print("Статистика по каждому файлу:")
        print(f"{'Файл':<15} {'Слово':<20} {'Количество':>12}")
        print("-" * 49)

        for filename, word, count in per_file_rows:
            print(f"{filename:<15} {word:<20} {count:>12}")
if __name__ == "__main__": main()