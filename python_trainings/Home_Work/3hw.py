#Задача 3.2: необходимо ввести 2 числа для определения максимального из них
from calendar import month


def function_max(a = int(input('a = ')), b = int(input('b = '))):
    return max(a, b)

print(function_max())

#Задача 3.3: принимает 2 числа и проверяет отличие на 135
x = int(input('x = '))
y = int(input('y = '))
if ((x - y) == 135) or ((y - x) == 135):
    print('YES')
else:
    print('NO')

#Задача 3.4: вывести сезон года в зависимости от номера месяца
def season_run(mon):
    if mon in range(3, 6):
        print('весна')
    elif mon in range(6, 9):
        print('лето')
    elif mon in range(9, 12):
        print('осень')
    elif mon == 12 or mon == 1 or mon == 2:
        print('зима')
    else:
        print('Введите корректный месяц')

season_run(int(input('Введите месяц: ')))

#Задача 3.5: 3 числа > 10
def num_num(i, j, k):
    if i > 10 and j > 10 and k > 10:
        print('YES')
    else:
        print('NO')
num_num(20, 13 , 18)

#Задача 3.6:
g = [5, 10, -3, -1, 15]
count = 0
for t in g:
    if t >= 0:
        count += 1
print(count)

#Задача 3.7: считает кол-во дней
def days(num_years, num_month):
    if num_years >= 0 and num_month >= 0:
        print((num_years * 12 * 29) + (num_month * 29))
    else:
        print('Неправильный ввод')
days(0, 4)