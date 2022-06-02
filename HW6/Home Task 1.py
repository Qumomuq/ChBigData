def instances_counter(cls):  # декоратор
    class Counter(cls):
        counter = 0

        def __init__(self):  # функция, вызываемая при создании экземпляра
            super().__init__()  # вызов функции
            Counter.counter += 1

        @classmethod  # возвращает количество экземпляров
        def get_created_instances(cls):
            print(Counter.counter)

        @classmethod  # сбрасывает значение counter
        def reset_instances_counter(cls):
            Counter.counter = 0
            print("Counter is 0")

    return Counter


@instances_counter
class User:
    pass


if __name__ == '__main__':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
