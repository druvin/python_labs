import argparse

from pathlib import Path

from src.lab_05.json_csv import json_to_csv, csv_to_json
from src.lab_05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных между JSON, CSV и XLSX")
    subparsers = parser.add_subparsers(dest = "command", required=True)

    json2csv_parser = subparsers.add_parser("json2csv", help = "JSON -> CSV")
    json2csv_parser.add_argument("--in", dest = "input", required = True, help = "Входной файл JSON")
    json2csv_parser.add_argument("--out", dest = "output", required = True, help = "Выходной файл CSV")

    csv2json_parser = subparsers.add_parser("csv2json", help = "CSV -> JSON")
    csv2json_parser.add_argument("--in", dest = "input", required = True, help = "Входной файл CSV")
    csv2json_parser.add_argument("--out", dest = "output", required = True, help = "Выходной файл JSON")

    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help = "CSV -> XLSX")
    csv2xlsx_parser.add_argument("--in", dest = "input", required = True, help = "Входной файл CSV")
    csv2xlsx_parser.add_argument("--out", dest = "output", required = True, help = "Выходной файл XLSX")

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(Path(args.input), Path(args.output))
        
        elif args.command == "csv2json":
            csv_to_json(Path(args.input), Path(args.output))
        
        elif args.command == "csv2xlsx":
            csv_to_xlsx(Path(args.input), Path(args.output))
    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input}")
    except UnicodeDecodeError:
        parser.error(f"Файл {args.input} написан в кодировке, отличной от UTF-8")
    except ValueError as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()