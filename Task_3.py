# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

import functions as gb

while (x := gb.get_number('Введите координаты X: ')) == 0:
    print('X не должно быть равно 0')
while (y := gb.get_number('Введите координаты Y: ')) == 0:
    print('Y не должно быть равно 0')
if y > 0:
    if x > 0: print('Точка находится в первой четверти')
    else: print('Точка находится во второй четверти')
else:
    if x < 0: print('Точка находится в третьей четверти')
    else: print('Точка находится в четвертой четверти')