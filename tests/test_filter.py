import pytest
from core.functions import FilterCommand
from tests.conftest import DATA


class TestFilter:
    def test_gt(self):
        cmd = FilterCommand('price>200')
        result = cmd.apply(DATA)
        assert len(result) == 1
        assert result[0]['name'] == 'item3'
    
    def test_ge(self):
        cmd = FilterCommand('price>=200')
        result = cmd.apply(DATA)
        assert len(result) == 2
        assert result[0]['name'] == 'item2'
    
    def test_lt(self):
        cmd = FilterCommand('price<200')
        result = cmd.apply(DATA)
        assert len(result) == 1
        assert result[-1]['name'] == 'item1'
    
    def test_le(self):
        cmd = FilterCommand('price<=200')
        result = cmd.apply(DATA)
        assert len(result) == 2
        assert result[-1]['name'] == 'item2'
    
    def test_eq_num(self):
        cmd = FilterCommand('price=300')
        result = cmd.apply(DATA)
        assert len(result) == 1
        assert result[0]['name'] == 'item3'
    
    def test_neq_num(self):
        cmd = FilterCommand('price!=300')
        result = cmd.apply(DATA)
        assert len(result) == 2
        assert result[-1]['name'] == 'item2'
    
    def test_eq_str(self):
        cmd = FilterCommand('brand=samsung')
        result = cmd.apply(DATA)
        assert len(result) == 1
        assert result[0]['name'] == 'item2'
    
    def test_neq_str(self):
        cmd = FilterCommand('brand!=samsung')
        result = cmd.apply(DATA)
        assert len(result) == 2
        assert result[-1]['name'] == 'item3'


class TestFilterErrors:
    def test_no_data(self):
        with pytest.raises(ValueError, match='Нет данных'):
            FilterCommand('price=200').apply({})
    
    def test_invalid_operator(self):
        with pytest.raises(ValueError, match='Некорректный оператор фильтрации'):
            FilterCommand('price@200').apply(DATA)
    
    def test_invalid_column(self):
        with pytest.raises(KeyError, match='Столбец "id" не найден в данных'):
            FilterCommand('id=13').apply(DATA)
