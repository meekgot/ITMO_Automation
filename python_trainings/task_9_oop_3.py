class Soda:

    def __init__(self, ing = None):
        self.ing = ing
#запись метода show_my_drink
    def show_my_drink(self):
        if self.ing:
            print(f'газировка и {self.ing}')

        else:
            print('Обычная гзировка')
#создание 2 объектов
drink1 = Soda()
drink2 = Soda('Малина')
#вызов метода show_my_drink для каждого объекта
drink1.show_my_drink()
drink2.show_my_drink()