from core.functions.base import Command


class AggregateCommand(Command):
    def __init__(self, instruction: str):
        if not '=' in instruction:
            raise ValueError('Формат aggregate: column=avg|min|max')
        self.col, self.op = instruction.split('=')
        self.col = self.col.strip()
        self.op = self.op.strip()

    def apply(self, data: list[dict]) -> list[dict]:
        self.check_column_exists(data, self.col)
        values = [float(row[self.col]) for row in data]

        if self.op == 'avg':
            result = sum(values) / len(values)
        elif self.op == 'min':
            result = min(values)
        elif self.op == 'max':
            result = max(values)
        else:
            raise ValueError('Неподдерживаемая операция')

        return [{f'{self.col}_{self.op}': result}]
