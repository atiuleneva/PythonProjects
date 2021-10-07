import random

print("Task #1")


class Date:
    def __init__(self, date):
        self.date = date

    def get_date(self, data):
        try:
            day, month, year = self.date.split("-")
            return int(day), int(month), int(year)
        except Exception as e:
            print(f'Не удалось выделить дату из строки. {e}')
            return 0, 0, 0

    @staticmethod
    def check_date(date_input):
        try:
            day, month, year = date_input
            if day not in range(1, 32):
                raise ValueError("День указан неверно")
            elif month not in range(1, 13):
                raise ValueError("Месяц указан неверно")
            elif year not in range(0, 2200):
                raise ValueError("Год указан неверно")
        except ValueError as e:
            print(e)
        else:
            print("Дата верна")


my_date = Date("06-10-202i")
day, month, year = my_date.get_date(my_date.date)
print(f'{day}-{month}-{year}')


print("Task #2")


class ZeroError(Exception):
    pass


def calc_1(a, b):
    if b == 0:
        raise ZeroError()
    return a / b


try:
    a_num = int(input("Введите число: "))
    b_num = int(input("Введите число: "))
    print(calc_1(a_num, b_num))
except ZeroError:
    print("На ноль делить нельзя!")

print("Task #3")


class NotNumberError(Exception):
    pass


num_list = []
while True:
    try:
        user = input("Введите число или строку: ")
        if user == 'stop':
            break

        num_list.append(int(user))
    except ValueError:
        try:
            raise NotNumberError()
        except NotNumberError:
            print("Введенное значение не является числом")

print(num_list)


print("Task #4")


class NoEquipment(Exception):
    pass


class Office_equipment_warehouse:
    def __init__(self):
        self.equipment = {}

    def pass_equipment(self, eq):
        if not (eq.equipment_type in self.equipment):
            self.equipment[eq.equipment_type] = []

        self.equipment[eq.equipment_type].append(eq)

    def take_eq(self, equipment_type):
        if not (equipment_type in self.equipment):
            raise NoEquipment

        if len(self.equipment[equipment_type]) > 0:
            return self.equipment[equipment_type].pop()

    def __str__(self):
        string = ""
        for k in self.equipment:
            string += f'\n\nType: {k} \n'
            string += f'=============================== \n'
            for eq in self.equipment[k]:
                string += f'{eq.title}, {eq.inventory_number} \n'
        return string


class Office_equipment:
    def __init__(self, equipment_type, title, inventory_number):
        self.equipment_type = equipment_type
        self.title = title
        self.inventory_number = inventory_number


class Printer(Office_equipment):
    def __init__(self, title, inventory_number, print_technology):
        super().__init__("Printer", title, inventory_number)
        self.print_technology = print_technology


class Scanner(Office_equipment):
    def __init__(self, title, inventory_number, resolution):
        super().__init__("Scanner", title, inventory_number)
        self.resolution = resolution


class Monitor(Office_equipment):
    def __init__(self, title, inventory_number, diagonal):
        super().__init__("Monitor", title, inventory_number)
        self.diagonal = diagonal


office_store = Office_equipment_warehouse()
printer_1 = Printer("Canon LJ-100", "15-ovp", "laser")
printer_2 = Printer("HP Ink Tank 115", "17-ovp", "laser")
printer_3 = Printer("EPSON L805", "19-ovp", "laser")
scanner_1 = Scanner("Kodak ScanMate i940", "23-ovp", "600x600 dpi")
scanner_2 = Scanner("Avision AD215", "25-ovp", "600x600 dpi")
scanner_3 = Scanner("Canon P-215II", "27-ovp", "600x600 dpi")
monitor_1 = Monitor("Xiaomi Mi Desktop Monitor", "29-ovp", "23.8")
monitor_2 = Monitor("Samsung F24T350FHI", "31-ovp", "23.8")
monitor_3 = Monitor("LG 29WN600", "33-ovp", "29")

office_store.pass_equipment(printer_1)
office_store.pass_equipment(printer_2)
office_store.pass_equipment(printer_3)
office_store.pass_equipment(scanner_1)
office_store.pass_equipment(scanner_2)
office_store.pass_equipment(scanner_3)
office_store.pass_equipment(monitor_1)
office_store.pass_equipment(monitor_2)
office_store.pass_equipment(monitor_3)

printer_for_managers = office_store.take_eq("Printer")
monitor_for_keepers = office_store.take_eq("Monitor")

print(f'{printer_for_managers.equipment_type} {printer_for_managers.title} выдан в отдел продаж')
print(f'{monitor_for_keepers.equipment_type} {monitor_for_keepers.title} выдан в отдел бухгалтерии')

print(office_store)


print("Task #7")


class Complex_num:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex_num(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex_num(self.real * other.real - self.imaginary * other.imaginary,
                           self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"


complex_num_1 = Complex_num(3, 5)
complex_num_2 = Complex_num(-2, 7)
print(f"Сумма: {complex_num_1 + complex_num_2}")
print(f"Произведение: {complex_num_1 * complex_num_2}")

num_1 = complex(3, 5)
num_2 = complex(-2, 7)

print(num_1 + num_2)
print(num_1 * num_2)























