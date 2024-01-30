# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Tree:
    def __init__(self, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"
        :param height: Высота дерева
        :param age: Возраст дерева
        Примеры:
        >>> tree = Tree(10.5, 5)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным числом")
        self.age = age


    def grow(self, growth: float):
        """
        Рост дерева
        :param growth: Прирост в высоте дерева
        Примеры:
        >>> tree = Tree(10.5, 5)
        >>> tree.grow(1.5)
        """
        pass


    def shed_leaves(self):
        """
        Сбросить листья с дерева
        Примеры:
        >>> tree = Tree(10.5, 5)
        >>> tree.shed_leaves()
        """
        pass


    def produce_fruits(self):
        """
        Породить плоды
        Примеры:
        >>> tree = Tree(10.5, 5)
        >>> tree.produce_fruits()
        """
        pass

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass




class Stadium:
    def __init__(self, capacity_area: float, occupied_area: float):
        """
        Создание и подготовка к работе объекта "Стадион"

        :param capacity_area: Количество мест на стадионе
        :param occupied_area: Количество занятых мест на стадионе

        Примеры:
        >>> stadium = Stadium(5000, 3800)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_area, (int, float)):
            raise TypeError("Количество мест на стадионе должно быть типа int или float")
        if capacity_area <= 0:
            raise ValueError("Количество мест на стадионе должно быть положительным числом")
        self.capacity_volume = capacity_area

        if not isinstance(occupied_area, (int, float)):
            raise TypeError("Количество занятых мест на стадионе должно быть int или float")
        if occupied_area < 0:
            raise ValueError("Количество занятых мест на стадионе не может быть отрицательным числом")
        self.occupied_volume = occupied_area

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стадион пустым
        :return: Является ли стадион пустым

        Примеры:
        >>> stadium = Stadium(5000, 3800)
        >>> stadium.is_empty_stadium()
        """
        ...

    def artists_stadium(self, artists: float) -> None:
        """
        :param people: Количество артистов на стадионе

        :raise ValueError: Если количество артистов на стадионе превышает количество занятых мест на стадионе, то вызываем ошибку

        Примеры:
        >>> stadium = Stadium(5000, 3800)
        >>> stadium.artists_stadium(26)
        """
        if not isinstance(artists, (int, float)):
            raise TypeError("Количество артистов должно быть типа int или float")
        if artists < 0:
            raise ValueError("Количество артистов должно быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

class Table:
    def __init__(self, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param length: Длина стола
        :param width: Ширина стола

        Примеры:
        >>> table = Table(120, 80)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина стола должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина стола должна быть положительным числом")
        self.capacity_volume = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть int или float")
        if width < 0:
            raise ValueError("Ширина стола не может быть отрицательным числом")
        self.occupied_volume = width

    def paint_table(self, color: str) -> None:
        """
        Функция для покраски стола

        :param color: Цвет для покраски

        Примеры:
        >>> table = Table(120, 80)
        >>> table.paint_table("blue")
        """
        ...

    def clean_table(self) -> None:
        """
        Функция для очистки стола

        :return: None

        Примеры:
        >>> table = Table(120, 80)
        >>> table.clean_table()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

