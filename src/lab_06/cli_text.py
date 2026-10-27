from src.lib.text import normalize, tokenize, count_freq, top_n
from pathlib import Path
import argparse

def cat_command(input_path:str, numbers: bool = False) -> None:
    path = Path(input_path)

    if not path.isfile():
        raise FileNotFoundError("Файл не найден")
    
    with open(path, "r", encoding='itf-8') as f:
        for num, line in enumerate(f, start = 1):
            if numbers:
                print(f"{num} {line}", end="")
            else:
                print(f"{line}", end="")
    

def stats_command(input_path: str, top: int = 5) -> None:
    path = Path(input_path)

    if not path.isfile():
        raise FileNotFoundError("Файл не найден")

    with open(path, "r", encoding='utf-8') as f:
        text = read(f)
    
    total_words = len(tokenize(normalize(text)))
    unique_words = len(count_freq(text))
    top_words = top_n(text, top)

    print(f'Всего слов: {total_words}')
    print(f'Уникальных слов: {unique_words}')
    print(f'Топ-{top}:')
    for w, c in top_words:
        print(f"{w}:{c}")
    
def main():
    parser = argparse.ArgumentParser(description = "CLI-утилиты")
    subparsers = parser.add_subparsers(dest = "command", required=True)

    cat_parser = subparsers.add_parser("cat", help = "Выводит содержание файла")
    cat_parser.add_argument("--input", required= True, help = "Считывает путь к входному файлу")
    cat_parser.add_argument("-n", action = "numbered_true", help = "Выводит номера строк файла")

    stats_parser = subparsers.add_parser("stats", help = "Частоты слов")
    stats_parser.add_argument("--input", required = True)
    stats_parser.add_argument("--top", type = int, default = 5)

    args = parser.parse_args()

    if args.command == "stats" and args.top < 1:
        parser.error("--top должен быть больше 0")
    try:
        if args.command == "cat":
            cat_command(args.input, args.n)

        elif args.command == "stats":
            stats_command(args.input, args.top)
    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input}")
    except UnicodeDecodeError:
        parser.error(f"Файл {args.input} написан в кодировке, отличной от UTF-8")

if __name__ == "__main__":
    main()
