#Создайте класс Input, принимающий 1 аргумент при инициализации (loc)
#Создайте объект serch (экземплыр класса Input)
#выведите в консоль значение аргумента loc, объекта search

class Input:
    def __init__(self, loc):
        self.loc = loc

search = Input('input#search')

print(search.loc)