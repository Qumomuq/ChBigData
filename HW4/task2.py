from os import path


def read_magic_number(location: str) -> bool:  # объявляем функцию с параметров (путь к файлу)
    if path.exists(location):
        with open(location, 'r') as f:  # С помощью контекстного менеджера открываем файл для чтения
            try:
                fst_line = float(f.readline())
                return 1. <= fst_line < 3.
            except Exception:
                raise ValueError
