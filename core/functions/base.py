class Command:
    '''Базовый класс команды'''
    def apply(self, data: list[dict]) -> list[dict]:
        '''Применение команды к данным'''
        raise NotImplementedError
    
    def check_column_exists(self, data: list[dict], column: str):
        '''Проверка существования столбца'''
        if not data:
            raise ValueError('Нет данных')
        if column not in data[0]:
            raise KeyError(f'Столбец "{column}" не найден в данных')
