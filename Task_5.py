# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import functions as gb

a = []
b = []
a.append(gb.get_number('Ведите координату X точки A:'))
a.append(gb.get_number('Ведите координату Y точки A:'))
b.append(gb.get_number('Ведите координату X точки B:'))
b.append(gb.get_number('Ведите координату Y точки B:'))
print('Расстояние меж точек A и B равно:', ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)