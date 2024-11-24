#Задача 4.1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def S(self):
        print(f'Площадь прямоугольника = {self.width * self.height}')

    def P(self):
        print(f'Периметр прямоугольника = {self.width + self.height + self.width + self.height}')

rec1 = Rectangle(2, 5)
rec2 = Rectangle(3, 3)
rec3 = Rectangle(4, 6)

rec1.S()
rec1.P()
rec2.S()
rec2.P()
rec3.S()
rec3.P()

#Задача 4.2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f'a + b = {self.a + self.b}')
    def subtraction(self):
        print(f'a - b = {self.a - self.b}')
    def multiplication(self):
        print(f'a * b = {self.a * self.b}')
    def division(self):
        print(f'a / b = {self.a / self.b}')

test = Math(int(input('a = ')), int(input('b = ')))
print(test.addition(), test.subtraction(), test.multiplication(), test.division())

#Задача 4.3
class Button:
    def __init__(self, name, type = 'Кнопка', loc = '\n'):
        self.name = name
        self.type = type
        self.loc = loc

    def click(self):
        return f"Клик по кнопке {self.name + ' ' + self.type + ' ' + self.loc}"

b1 = Button('Text Box')
b2 = Button('Check Box')
b3 = Button('Radio Button')
b4 = Button('Web Tables')
b5 = Button('Buttons')
b6 = Button('Links')
b7 = Button('Broken Links - Images')
b8 = Button('Upload and Download')
b9 = Button('Dynamic Properties')

print(b1.click(), b2.click(), b3.click(), b4.click(), b5.click(), b6.click(), b7.click(), b8.click(), b9.click())