import subprocess
import os

DATA = [
    {'name': 'item1', 'price': '100', 'brand': 'apple'},
    {'name': 'item2', 'price': '200', 'brand': 'samsung'},
    {'name': 'item3', 'price': '300', 'brand': 'xiaomi'}
]


def run_cli(*args):
    if os.path.exists(f'{os.curdir}/core/main.py'):
        result = subprocess.run(
            ['python', '-m', 'core.main', *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        return result
    else:
        raise FileNotFoundError('Скрипт запуска не найден')
