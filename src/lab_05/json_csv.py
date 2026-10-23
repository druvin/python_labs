import json, csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    in_data_json = Path(json_path)
    out_data_csv = Path(csv_path)

    if not in_data_json.is_file():
        raise FileNotFoundError(f"Файл не найден: {in_data_json}")

    if in_data_json.suffix.lower() != ".json":
        raise ValueError("Входной файл должен быть формата .json")

    if out_data_csv.suffix.lower() != ".csv":
        raise ValueError("Выходной файл должен быть формата .csv")

    with open(in_data_json, encoding='utf-8') as f:
        try: data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError("Пустой файл или неподдерживаемая структура") from e

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Пустой файл или неподдерживаемая структура")

    for element in data:
        if not isinstance(element, dict):
            raise ValueError("JSON должен содержать список словарей")

    headers = list(dict.fromkeys(key for row in data for key in row))

    if len(headers) == 0:
        raise ValueError("Пустой файл или неподдерживаемая структура")

    for header in headers:
        if not header.strip():
            raise ValueError("Заголовки не должны быть пустыми")

    with out_data_csv.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(headers)

        for el in data:
            values = [el.get(header,'') for header in headers]
            writer.writerow(values)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    in_data_csv = Path(csv_path)
    out_data_json = Path(json_path)
    if not in_data_csv.is_file():
        raise FileNotFoundError(f"Файл не найден: {in_data_csv}")

    if in_data_csv.suffix.lower() != ".csv":
        raise ValueError("Входной файл должен быть формата .csv")

    if out_data_json.suffix.lower() != ".json":
        raise ValueError("Выходной файл должен быть формата .json")
    
    with in_data_csv.open("r", newline="", encoding='utf-8') as in_file:
        try:
            reader = csv.DictReader(in_file, strict=True)
            headers = reader.fieldnames
            
            if headers is None or len(headers) == 0:
                raise ValueError("Пустой CSV или отсутствует заголовок")
            for header in headers:
                if not header.strip():
                    raise ValueError("Заголовки не должны быть пустыми")
            if len(headers) != len(set(headers)):
                raise ValueError("Названия столбцов не должны повторяться")
            result = list(reader)

            for el in result:
                if None in el or None in el.values():
                    raise ValueError("Количество полей не совпадает с заголовком")
        except csv.Error as e:
            raise ValueError("Некорректный формат CSV") from e
    with out_data_json.open("w", encoding='utf-8') as out_file:
        json.dump(result, out_file, ensure_ascii=False, indent=2)