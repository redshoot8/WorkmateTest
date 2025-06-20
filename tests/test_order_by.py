import pytest
from core.functions import OrderByCommand
from tests.conftest import DATA


class TestOrderBy:
    def test_asc(self):
        cmd = OrderByCommand('price=asc')
        result = cmd.apply(DATA)
        assert len(result) == 3
        assert result == sorted(result, key=lambda x: float(x['price']))
    
    def test_desc(self):
        cmd = OrderByCommand('price=desc')
        result = cmd.apply(DATA)
        assert len(result) == 3
        assert result == sorted(result, key=lambda x: -float(x['price']))


class TestOrderByErrors:
    def test_no_data(self):
        with pytest.raises(ValueError, match='Нет данных'):
            OrderByCommand('price=asc').apply({})
    
    def test_invalid_format(self):
        with pytest.raises(ValueError, match='Формат order_by: column=asc|desc'):
            OrderByCommand('price@desc').apply(DATA)
    
    def test_invalid_operation(self):
        with pytest.raises(ValueError, match='Неподдерживаемая операция'):
            OrderByCommand('price=random').apply(DATA)
        
    def test_invalid_column(self):
        with pytest.raises(KeyError, match='Столбец "id" не найден в данных'):
            OrderByCommand('id=asc').apply(DATA)
