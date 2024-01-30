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

