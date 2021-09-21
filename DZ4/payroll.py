from sys import argv


def calc_payroll(_output_in_hours, _rate, _premium):
    print("Задание №1")

    _output_in_hours = int(_output_in_hours)
    _rate = int(_rate)
    _premium = int(_premium)

    payroll = ((_output_in_hours * _rate) + _premium)
    print("Зарплата: ", payroll)


script_name, output_in_hours, rate, premium = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", output_in_hours)
print("Ставка в час: ", rate)
print("Премия: ", premium)

calc_payroll(output_in_hours, rate, premium)

