class Page:
    def __init__(self, url):
        self.url = url
#реализуем метод get
    def get(self):
        print(self.url)
#создаем объект home
home = Page('https://demoqa.com/')
#вызываем метод get
home.get()