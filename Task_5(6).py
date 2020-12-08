class Stationery:
    def __init__(self,title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки ')

class Pen(Stationery):
    def draw(self):
        print(f'Рисуем с помощью {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем с помощью {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Рисуем с помощью {self.title}')



handle = Handle('handle')
pen = Pen('pen')
pencil = Pencil('pencil')
handle.draw()
pen.draw()
pencil.draw()