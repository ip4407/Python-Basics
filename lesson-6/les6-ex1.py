"""
Урок 6.
Задание 1.

Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав
экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его
нарушении выводить соответствующее сообщение и завершать скрипт.

"""

from time import sleep


class TrafficLight:

    __color = 'red'

    def running(self):
        if self.__color == 'red':
            print('red')
            sleep(7)
            print('yellow')
            sleep(2)
            print('green\n')
            sleep(3)
        else:
            print('Error!\nAn invalid value for the private color attribute is set.')


traffic_light = TrafficLight()
traffic_light.running()

traffic_light.running()

traffic_light._TrafficLight__color = 'green'
traffic_light.running()
