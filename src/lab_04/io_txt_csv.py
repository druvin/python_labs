import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текст из файла в указанной кодировке."""
    p = Path(path)
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