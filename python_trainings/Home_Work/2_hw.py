# Задача 1
def task_1(a: int = 6,
           b: float = 0.5,
           c: str = 'green',
           d: list = [1,2],
           e: bool = True) ->str:
    return type(a), type(b), type(c), type(d), type(e)#возвращает тип данных каждой переменной

print(task_1())

#Задача 2
def task_2(a: list = [1, 2, 3, 5, 8, 13, 21]):
    return a[0:3]#возвращает первые 3 значения последовательности

print(task_2())

#Такая последовательность называется Последовательностью Фибоначчи

#Задача 3
def task_3(x = int(input('введи число: '))):
    return x**2#возвращает квадрат введенного числа

print(task_3())