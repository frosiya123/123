#Напишите программу, которая по заданному номеру четверти,
#показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти от 1 до 4 = '))
if a == 1:
    print('x = от 1 до n; y = от 1 до n')
elif a == 2:
    print('x = от -1 до -n; y = от 1 до n')
elif a == 3:
    print('x = от -1 до -n; y = от -1 до -n')
elif a == 4:
    print('x = от 1 до n; y = от -1 до -n')