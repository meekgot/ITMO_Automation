num = 3

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

num2 = 0

if num2 >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

num3 = -5

if num3 >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

str_1 = 'test'
str_2 = 'test1'

if str_1[0:4] == str_2[0:4]:
    print('Да')
else:
    print('Нет')

def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print("Да")
    else:
        print('Нет')

task_yes_no(str_1 = 'test', str_2 = 'test1')