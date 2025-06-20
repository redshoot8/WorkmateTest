from core.functions.base import Command
from core.utils import try_float_cast


class OrderByCommand(Command):
    def __init__(self, instruction: str):
        if '=' not in instruction:
            raise ValueError('Формат order_by: column=asc|desc')
        self.col, self.direction = instruction.split('=')
        self.col = self.col.strip()
        self.direction = self.direction.strip().lower()
        if self.direction != 'asc' and self.direction != 'desc':
            raise ValueError('Неподдерживаемая операция')

    def apply(self, data: list[dict]) -> list[dict]:
        self.check_column_exists(data, self.col)
        return sorted(data, key=lambda row: try_float_cast(row[self.col]), reverse=(self.direction == 'desc'))
