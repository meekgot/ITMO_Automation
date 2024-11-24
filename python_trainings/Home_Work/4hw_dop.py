class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def Start(self):
        print('Автомобиль заведен')
    def End(self):
        print('Автомобиль заглушен')
    def YearRelease(self):
        print(f'{self.year} года выпуска')
    def AutoType(self):
        print(f'Имеет тип {self.type}')
    def AutoColor(self):
        print(f'Автомобиль {self.color} цвета')

A1 = Car('оранжевого', 'седан', 1999)

print(A1.AutoColor(), A1.AutoType(), A1.YearRelease())
print(A1.Start())