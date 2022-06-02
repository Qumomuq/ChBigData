class FileValueError(Exception):
    pass


class KeyValueStorage:

    def __setitem__(self, key, item):  # методы доступа к атрибуту через квадратные скобки
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __init__(self, path: str):
        with open(path, 'r') as file:  # открытие файла
            for line in file:
                try:  # проверяем ключ = число?
                    int(line.split('=')[0])
                    raise FileValueError('Key can not be an integer.')
                except ValueError:  # если не число
                    key = line.split('=')[0]
                    try:
                        value = int(line.split('=')[1])
                    except ValueError:
                        value = line.split('=')[1].strip()
                    if key not in dir(self):  # проверка оригинальности атрибута для его создания
                        setattr(self, key, value)
                        self[key] = value
