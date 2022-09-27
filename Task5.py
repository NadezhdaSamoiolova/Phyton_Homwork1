##### ** Task 5 ** #####    
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

print('Input coordinates of point A')
x_A = float(input ('x_A: '))
y_A = float(input ('y_A: '))

print('Input coordinates of point B')
x_B = float(input ('x_B: '))
y_B = float(input ('y_B: '))

import math
result = math.sqrt((x_B - x_A) ** 2 + (y_B - y_A) ** 2)
print(round(result, 2))
