import csv


def read_csv(filepath: str) -> list[dict]:
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)
