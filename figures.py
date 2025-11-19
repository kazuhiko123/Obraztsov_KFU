import math
from abc import ABC, abstractmethod
from math import radians
from tkinter import EventType

pi = math.pi

"""абстрактный класс"""
class shape(ABC):
    @abstractmethod
    def calculate_area(self):

        pass
    @abstractmethod
    def calculate_perimetr(self):

        pass

    def info(self):
        return 'Фигура'



"""Квадрат"""
class square(shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2

    def calculate_perimetr(self):
        return self.side*4

    def info(self):
        return 'Фигура - квадрат'

    def __str__(self):
        return f'Квадрат со стороной {self.side} см.'

    def __len__(self):
        return int(self.calculate_perimetr())

    def __eq__(self, other):
        if not isinstance(other, square):
            return False
        return self.side == other.side

"""Окружность"""
class circle(shape):
    def __init__(self, radius):
        self.radius= radius

    def calculate_area(self):
        return pi * self.radius**2

    def calculate_perimetr(self):
        return 2*pi*self.radius

    def info(self):
        return 'Фигура - круг'

    def __str__(self):
        return f'Круг с радиусом {self.radius} см'

    def __len__(self):
        return int(self.calculate_perimetr())

    def __eq__(self, other):
        if not isinstance(other, circle):
            return False
        return self.radius == other.radius


class geometrycalculator:
    @staticmethod
    def validate_positive(number):
        if number <=0:
            raise ValueError('Число должно быть положительным')
        return True

    @staticmethod
    def calculate_diagonal(length, width):
        geometrycalculator.validate_positive(length)
        geometrycalculator.validate_positive(width)
        return (length**2 + width**2)**0.5

    @staticmethod
    def is_larger(shape1, shape2):
        if not isinstance(shape1, shape) or not isinstance(shape2, shape):
            raise TypeError('оба аргумента должны быть фигурами')
        return shape1.calculate_area() > shape2.calculate_area()

if __name__ =='__main__':
    square1 = square(2)
    square2 = square(4)
    circle1 = circle(1)
    circle2= circle(3)

    """Проверка работы"""
    print(f'{square1.info()}: площадь = {square1.calculate_area()}, периметр = {square1.calculate_perimetr()}')
    print(f'{square2.info()}: площадь = {square2.calculate_area()}, периметр = {square2.calculate_perimetr()}')
    print(f'{circle1.info()}: площадь = {circle1.calculate_area()}, длинна окружности = {circle1.calculate_perimetr()}')
    print(f'{circle2.info()}: площадь = {circle2.calculate_area()}, длинна окружности = {circle2.calculate_perimetr()}')

    """Проверка базовых методов"""
    print(f'__str__: {square1}')
    print(f'__str__: {square2}')
    print(f'__str__: {circle1}')
    print(f'__str__: {circle2}')

    '''проверка магических методов'''
    print(f'Периметр квадрата: {len(square1)}')
    print(f'Периметр квадрата: {len(square2)}')
    print(f'Длинна окружности: {len(circle1)}')
    print(f'Длинна окружности: {len(circle2)}')

    square_eq = square(2)
    circle_eq = circle(1)
    print(f'square1 == square_eq: {square1 == square_eq}')
    print(f'circle1 == circle_eq: {circle1 == circle_eq}')

    print(f'circle1 == square1: {circle1 == square1}')

    """Тестирование статических методов"""
    diagonal =geometrycalculator.calculate_diagonal(3, 4)
    print(f'Диагональ прямоугольника 3х4: {diagonal} (Ожидается 5.0)')

    is_larger =geometrycalculator.is_larger(square1, circle1)
    print(f'square1 больше circle1: {is_larger}')
