"""
Урок 6.
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


class Stationery:
    title = 'Канцтовары'

    def draw(self):
        print('Запуск отрисовки.')


class Pencil(Stationery):

    def draw(self):
        print('Рисование карандашом.')


class Handle(Stationery):

    def draw(self):
        print('Рисование маркером.')


class Pen(Stationery):

    def draw(self):
        print('Рисование ручкой.')


stat = Stationery()
print(Stationery.title)
stat.draw()

pen1 = Pen()
pen1.draw()

pencil1 = Pencil()
pencil1.draw()

handle1 = Handle()
handle1.draw()
