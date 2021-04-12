"""
Урок 7.
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def cloth_consumption(self):  # Расчет расхода ткани
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def cloth_consumption(self):
        coat_cloth_consumption = 2 * self.size + 0.3  # Расчет расхода ткани для пальто
        return coat_cloth_consumption


class Suit(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def cloth_consumption(self):
        suit_cloth_consumption = self.height / 6.5 + 0.5  # Расчет расхода ткани для костюма
        return suit_cloth_consumption


coat1 = Coat(48)
print(f'Расход ткани для пальто размера {coat1.size} = {coat1.cloth_consumption:.2f}')

suit1 = Suit(178)
print(f'Расход ткани для костюма размера {suit1.height} = {suit1.cloth_consumption:.2f}')

print(f'Общий расход ткани = {coat1.cloth_consumption + suit1.cloth_consumption:.2f}')
