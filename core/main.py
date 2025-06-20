import sys
from tabulate import tabulate
from core.cli import parse_args
from core.reader import read_csv
from core.functions import FilterCommand, AggregateCommand, OrderByCommand


def main():
    args = parse_args()
    
    try:
        data = read_csv(args.file)
    except FileNotFoundError:
        print('Файл не найден', file=sys.stderr)
        sys.exit(1)

    try:
        if args.where:
            data = FilterCommand(args.where).apply(data)
        if args.order_by:
            data = OrderByCommand(args.order_by).apply(data)
        # Агрегация в конце
        if args.aggregate:
            data = AggregateCommand(args.aggregate).apply(data)
            
        print(tabulate(data, headers='keys', tablefmt='grid'))
    except Exception as e:
        print(f'Ошибка: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
