##### ** Task 3 ** #####
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Input x: '))
y = int(input('Input y: '))

if x > 0 and y > 0:
    print('Your point is in the quarter of coordinate plane Nr. 1 ')
elif x < 0 and y > 0:
    print('Your point is in the quarter of coordinate plane Nr. 2 ')
elif x < 0 and y < 0:
    print('Your point is in the quarter of coordinate plane Nr. 3 ')
elif x > 0 and y < 0:
    print('Your point is in the quarter of coordinate plane Nr. 4 ')
elif x == 0:
    print('Your point is on coordinate axis "y"')
elif y == 0:
    print('Your point is on coordinate axis "x"')