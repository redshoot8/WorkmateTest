import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='CSV фильтрация и агрегация')
    parser.add_argument('--file', required=True, help='Путь к CSV-файлу')
    parser.add_argument('--where', help='Фильтрация, формат: column[operator]value, например price>=500')
    parser.add_argument('--aggregate', help='Агрегация, формат: column=operation, например price=avg')
    parser.add_argument('--order-by', help='Сортировка, формат: column=order, напрмиер price=desc')
    return parser.parse_args()
