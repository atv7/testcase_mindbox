from typing import Union


class Geometry:
    @staticmethod
    def circle_area(radius: Union[int, float]) -> float:
        """
        Вычисляет площадь круга по радиусу.

        :param radius: радиус круга
        :return: площадь круга
        """
        if radius < 0:
            raise ValueError("Радиус не может быть меньше 0")
        return 3.14 * radius**2  # Площадь круга

    @staticmethod
    def triangle_area(a: Union[int, float],
                      b: Union[int, float],
                      c: Union[int, float]) -> float:
        """
        Вычисляет площадь триугольника по трём сторонам.
        :param a: сторона треугольника
        :param b: сторона треугольника
        :param c: сторона треугольника
        :return: площадь треугольника
        """

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Длины сторон должны быть положительными числами")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Невозможно построить треугольник с заданными сторонами")

        # Полупериметр треугольника
        s = (a + b + c) / 2

        # Формула Герона для площади треугольника
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area  # площадь треугольника

    @staticmethod
    def is_right_triangle(a: Union[int, float],
                          b: Union[int, float],
                          c: Union[int, float]) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным по теореме Пифагора.

        :param a: сторона треугольника
        :param b: сторона треугольника
        :param c: сторона треугольника
        :return: True или False
        """
        sides = [a, b, c]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

    @staticmethod
    def area(*args: Union[int, float]) -> float:
        """
        Вычисляет площадь фигуры без знания её типа.
        Принимает произвольное количество аргументов.

        :param args: радиус круга или стороны треугольника
        :return:
        """
        if len(args) == 1:
            # Если передан один аргумент, предполагаем, что это радиус круга
            return Geometry.circle_area(args[0])
        elif len(args) == 3:
            # Если переданы три аргумента, предполагаем, что это стороны треугольника
            return Geometry.triangle_area(*args)
        else:
            raise ValueError("Неподдерживаемое количество аргументов")



