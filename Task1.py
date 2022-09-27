##### ** Task 1 ** #####
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input('Input a number from 1 to 7: \n'))
if 1 <= a <= 5:
    print('No. This is a weekday!')
elif a == 6 or a == 7:
    print('Yes. This is a weekend')
else:
    print('You entered a wrong number')
    