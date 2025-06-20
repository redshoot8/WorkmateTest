import pytest
from tests.conftest import run_cli


class TestGeneral:
    def test_filter_price_gt(self):
        result = run_cli('--file', 'test.csv', '--where', 'price>500')
        assert 'iphone 15 pro' in result.stdout
        assert 'redmi' not in result.stdout

    def test_aggregate_rating_avg(self):
        result = run_cli('--file', 'test.csv', '--aggregate', 'rating=avg')
        assert 'rating_avg' in result.stdout
        assert '4.6' in result.stdout or '4.675' in result.stdout

    def test_order_by_price(self):
        result = run_cli('--file', 'test.csv', '--order-by', 'price=asc')
        assert result.stdout.index('redmi note 12') < result.stdout.index('poco x5 pro')

    def test_invalid_column(self):
        result = run_cli('--file', 'test.csv', '--where', 'badcolumn=100')
        assert result.returncode != 0

    def test_combined(self):
        result = run_cli('--file', 'test.csv', '--where', 'brand=xiaomi', '--order-by', 'rating=desc', '--aggregate', 'price=max')
        assert 'price_max' in result.stdout
        assert '299' in result.stdout
