num_float = 3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

num_float_2 = 0

if num_float_2 > 0:
    print('Положительное число')
elif num_float_2 == 0:
    print('Ноль')
else:
    print('Отрицательное число')

num_float_3 = -4.5

if num_float_3 > 0:
    print('Положительное число')
elif num_float_3 == 0:
    print('Ноль')
else:
    print('Отрицательное число')

permit_print = True
num = 2

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_rang(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('Вы - бакалавр')
    elif year_of_study in range(5, 7):
        print('Вы - магистр')
    elif 7 <= year_of_study <= 9:
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

student_rang(11)

def number(num2):
    if num2 > 100 or num2 <-100:
        print('-')
    else:
        print('+')
number(105)

a = 10

if a >100 or a < -100:
    print('-')
else:
    print('+')
    