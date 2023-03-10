# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

import functions as gb

while not (1 <= (day := gb.get_int('Введите номер дня недели: ')) <= 7):
    print('Число должно быть в диапозоне от 1 до 7')
if day in (6, 7): print('Ура! Выходной! :)')
else: print('Опять трудовые будни :(')