import operator
from core.functions.base import Command
from core.utils import try_float_cast


OPERATORS = {
    '>=': operator.ge,
    '<=': operator.le,
    '!=': operator.ne,
    '>': operator.gt,
    '<': operator.lt,
    '=': operator.eq
}


class FilterCommand(Command):
    def __init__(self, condition: str):
        self.condition = condition

    def apply(self, data: list[dict]) -> list[dict]:
        for op_str in sorted(OPERATORS.keys(), key=lambda x: -len(x)):
            if op_str in self.condition:
                col, val = self.condition.split(op_str, 1)
                col, val = col.strip(), val.strip()
                
                self.check_column_exists(data, col)
                op_func = OPERATORS[op_str]

                def match(row):
                    left = try_float_cast(row[col])
                    right = try_float_cast(val)
                    try:
                        return op_func(left, right)
                    except Exception:
                        return False

                return [row for row in data if match(row)]

        raise ValueError('Некорректный оператор фильтрации')
