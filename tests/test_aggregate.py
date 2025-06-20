import pytest
from core.functions import AggregateCommand
from tests.conftest import DATA


class TestAggregate:
    def test_avg(self):
        cmd = AggregateCommand('price=avg')
        result = cmd.apply(DATA)
        assert len(result) == 1
        assert result[0]['price_avg'] == 200
    
    def test_min(self):
        cmd = AggregateCommand('price=min')
        result = cmd.apply(DATA)
        assert len(result) == 1
        assert result[0]['price_min'] == 100
    
    def test_max(self):
        cmd = AggregateCommand('price=max')
        result = cmd.apply(DATA)
        assert len(result) == 1
        assert result[0]['price_max'] == 300


class TestAggregateErrors:
    def test_no_data(self):
        with pytest.raises(ValueError, match='Нет данных'):
            AggregateCommand('price=avg').apply({})
    
    def test_invalid_format(self):
        with pytest.raises(ValueError, match='Формат aggregate: column=avg|min|max'):
            AggregateCommand('price@max').apply(DATA)
    
    def test_invalid_operation(self):
        with pytest.raises(ValueError, match='Неподдерживаемая операция'):
            AggregateCommand('price=medium').apply(DATA)
        
    def test_invalid_column(self):
        with pytest.raises(KeyError, match='Столбец "id" не найден в данных'):
            AggregateCommand('id=min').apply(DATA)
