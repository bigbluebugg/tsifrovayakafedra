class Animal:
    """
    Базовый класс Животное.

    Attributes:
    - name (str): Имя животного.
    - age (int): Возраст животного.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        """
        Метод, который должен быть реализован в дочерних классах для издания звука.

        Returns:
            str: Звук, издаваемый животным.
        """
        pass

    def move(self, distance: int):
        """
        Движение животного на заданное расстояние.

        Args:
            distance (int): Расстояние, на которое перемещается животное.
        """
        print(f"{self.name} передвигается на расстояние {distance}.")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, возраст {self.age} лет."


class Dog(Animal):
    """
    Дочерний класс Собака, наследуется от базового класса Animal.
    """

    def make_sound(self):
        return "Гав-гав!"

    def wag_tail(self):
        """
        Метод только для собак. Махание хвостом.

        Returns:
            str: Действие собаки.
        """
        pass


class Cat(Animal):
    """
    Дочерний класс Кошка, наследуется от базового класса Animal.
    """

    def make_sound(self):
        return "Мяу!"

    def climb_tree(self):
        """
        Метод только для кошек. Подняться на дерево.

        Returns:
            str: Действие кошки.
        """
        pass


if __name__ == "__main__":
    # Создаем экземпляры классов
    dog = Dog("Бобик", 3)
    cat = Cat("Мурка", 2)

    # Демонстрация работы методов
    print(dog)
    print(cat)

    dog.move(10)
    cat.move(5)

    print(dog.make_sound())
    print(cat.make_sound())