from src.lib.text import normalize, tokenize, count_freq, top_n
from Pathlib import Path
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
    





if __name__ == "__main__":
    main()
