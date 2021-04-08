"""
Урок 6.
Задание 4.

Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""

from random import randint

def current_speed_car():
    return randint(0, 250)

def turn_car():
    car_direction = ['left', 'right', 'back']
    return car_direction[randint(0, 2)]


class Car:
    
    def __init__(self, speed=0, color=None, name='Car', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        return "The car's gone."

    def car_stop(self):
        self.speed = 0
        return 'The car stopped.'
    
    def car_turn(self, direction):
        return f'The car turned {direction}.'
    
    def show_speed(self):
        return f'Current car speed {self.speed} km/h.'
    
    def ispolice(self):
        ispolice = 'Yes' if self.is_police == True else 'No'
        return ispolice

class TownCar(Car):
    def __init__(self, speed=0, color='Black', name='TownCar', is_police=False):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if self.speed > 60:
            print(f'You are driving over the maximum speed limit of 60 km/h')
        return f'Current car speed {self.speed} km/h'


class SportCar(Car):
    def __init__(self, speed=0, color='Red', name='SportCar', is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed=0, color='Orange', name='WorkCar', is_police=False):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if self.speed > 40:
            print(f'You are driving over the maximum speed limit of 40 km/h')
        return f'Current car speed {self.speed} km/h'


class PoliceCar(Car):
    def __init__(self, speed=0, color='white and blue', name='PoliceCar', is_police=True):
        super().__init__(speed, color, name, is_police)


car1 = Car(current_speed_car(), 'Green', 'Car')
print('------- Класс "Car" -------')
print(f'Car is {car1.name}')
print(f'Car color: {car1.color}')
print(f'Car speed: {car1.speed}')
print(f'Is that a police car? {car1.ispolice()}')
print(car1.car_go())
print(car1.car_turn(turn_car()))
print(car1.car_turn(turn_car()))
print(car1.show_speed())
print(car1.car_stop())
print(car1.show_speed())
print('-------------------------------\n')

town_car1 = TownCar(current_speed_car())
print('------- Класс "TownCar" -------')
print(f'Car is {town_car1.name}')
print(f'Car color: {town_car1.color}')
print(f'Car speed: {town_car1.speed}')
print(f'Is that a police car? {town_car1.ispolice()}')
print(town_car1.car_go())
print(town_car1.car_turn(turn_car()))
print(town_car1.car_turn(turn_car()))
print(town_car1.show_speed())
print(town_car1.car_stop())
print(town_car1.show_speed())
print('-------------------------------\n')

sport_car1 = SportCar(current_speed_car(), 'Yellow', 'Lamborgini')
print('------- Класс "SportCar" -------')
print(f'Car is {sport_car1.name}')
print(f'Car color: {sport_car1.color}')
print(f'Car speed: {sport_car1.speed}')
print(f'Is that a police car? {sport_car1.ispolice()}')
print(sport_car1.car_go())
print(sport_car1.car_turn(turn_car()))
print(sport_car1.car_turn(turn_car()))
print(sport_car1.show_speed())
print(sport_car1.car_stop())
print(sport_car1.show_speed())
print('-------------------------------\n')

police_car1 = PoliceCar(current_speed_car())
print('------- Класс "PoliceCar" -------')
print(f'Car is {police_car1.name}')
print(f'Car color: {police_car1.color}')
print(f'Car speed: {police_car1.speed}')
print(f'Is that a police car? {police_car1.ispolice()}')
print(police_car1.car_go())
print(police_car1.car_turn(turn_car()))
print(police_car1.car_turn(turn_car()))
print(police_car1.show_speed())
print(police_car1.car_stop())
print(police_car1.show_speed())
print('-------------------------------\n')

work_car1 = WorkCar(current_speed_car())
print('------- Класс "WorkCar" -------')
print(f'Car is {work_car1.name}')
print(f'Car color: {work_car1.color}')
print(f'Car speed: {work_car1.speed}')
print(f'Is that a police car? {work_car1.ispolice()}')
print(work_car1.car_go())
print(work_car1.car_turn(turn_car()))
print(work_car1.car_turn(turn_car()))
print(work_car1.show_speed())
print(work_car1.car_stop())
print(work_car1.show_speed())
print('-------------------------------\n')
