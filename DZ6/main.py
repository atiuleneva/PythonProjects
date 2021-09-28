import time
print("Task #1")


class TrafficLight:
    RED = 0
    YELLOW = 1
    GREEN = 2
    colors = {RED: "red", YELLOW: 'yellow', GREEN: "green"}

    def __init__(self):
        self.__color = self.RED

    def running(self):
        for i in range(3):
            if i > 0:
                time.sleep(5)
            self.__color = self.RED
            print(self.colors[self.__color])
            time.sleep(7)
            self.__color = self.YELLOW
            print(self.colors[self.__color])
            time.sleep(2)
            self.__color = self.GREEN
            print(self.colors[self.__color])


traffic_light = TrafficLight()
traffic_light.running()


print("Task #2")


class Road:
    MASS_OF_ASPHALT = 25 / 1000

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, h):
        mass = self._length * self._width * self.MASS_OF_ASPHALT * h
        print(f'{round(mass)} тонн асфальта расходуется при толщине {h} см')


road_6 = Road(1000, 50)
road_6.mass(5)


print("Task #3")


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


workers = [
    Position("Ivan", "Ivanov", "Director", 150000, 50000),
    Position("Anna", "Ivanova", "Keeper", 50000, 5000),
    Position("Petr", "Petrov", "Manager", 60000, 10000)
]

for worker in workers:
    print(f'{worker.get_full_name()} {worker.position}, income: {worker.get_total_income()}')


print("Task #4")

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f'Ваша скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Вы превысили скорость на {self.speed - 60}")


class SportCar(Car):
    def skidding(self):
        print(f'{self.name} на {self.speed} км/ч совершил супер дрифт')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Вы превысили скорость на {self.speed - 40}")


class PoliceCar(Car):
    def penalty(self, cars):
        for car in cars:
            print(f'{self.name} оштрафовал машину {car.name}')
            if car.speed - 60 > 60:
                print(f"{self.name} забрал права у машины {car.name} за превышение на {car.speed - 60} км/ч")


car_1 = WorkCar(80, "green", "workCar", False)
car_1.show_speed()

car_2 = TownCar(80, "blue", "martlet", False)
car_2.show_speed()

sport = SportCar(125, "red", "speedy", False)
sport.skidding()

police = PoliceCar(60, "white", "cop1", True)
police.penalty([car_2, car_1, sport])


print("Task #5")


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def __init__(self):
        super().__init__("pen")

    def draw(self):
        print(f'Запуск отрисовки {self.title}, я ручка')


class Pencil(Stationery):
    def __init__(self):
        super().__init__("pencil")

    def draw(self):
        print(f'Запуск отрисовки {self.title}, я карандаш')

    def drawText(self, text):
        print(f'{self.title}: {text}')


class Handle(Stationery):
    def __init__(self):
        super().__init__("handle")

    def draw(self):
        print(f'Запуск отрисовки {self.title}, я маркер')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()





