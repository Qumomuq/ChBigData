def backspace_compare(first: str, second: str):
    def backspace(line: str):
        if '#' in line:
            if line.startswith('#'):  # удаляем все # с помощью рекурсии
                line_changed = line.replace('#', '', 1)
                backspace(line_changed)

            line_list = list(line)  # преобразуем строку в список
            for key, value in enumerate(line_list):
                if value == '#':
                    line_list[key - 1] = ''
                    line_list[key] = ''
            line_list.remove('')
            return ''.join(line_list)  # преобразуем в строку возращаемый список
        else:
            return line

    return backspace(first) == backspace(second)
