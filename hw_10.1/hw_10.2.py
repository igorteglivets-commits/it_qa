from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        """Площа фігури"""
        pass

    @abstractmethod
    def perimeter(self):
        """Периметр фігури"""
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side


class Triangle(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return (3 ** 0.5 / 4) * (self.__side ** 2)

    def perimeter(self):
        return 3 * self.__side


class Pentagon(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        import math
        return (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.__side ** 2)

    def perimeter(self):
        return 5 * self.__side


figures = [
    Square(4),
    Triangle(3),
    Pentagon(2)
]

for f in figures:
    print(f"Фігура: {f.__class__.__name__}")
    print(f"  Площа: {f.area():.2f}")
    print(f"  Периметр: {f.perimeter():.2f}")
    print("-" * 30)
