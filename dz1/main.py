# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

SEC_IN_HOUR = 3600
SEC_IN_MIN = 60


def task1():
    print("Задание №1")
    int_var = 10
    str_var = "hello Python"

    print(f'My int_var: {int_var}, My str_var: {str_var}')

    a = int(input("Введите число: "))
    print(f'Вы ввели число {a}')
    b = input("Верно? ")
    print(f'Вы ответили: "{b}"')


def task2():
    print("Задание №2")
    # input
    time = int(input("Введите время в секундах: "))
    # calc hours
    h = int(time / SEC_IN_HOUR)
    time = int(time - (SEC_IN_HOUR * h))
    # calc minutes
    m = int(time / SEC_IN_MIN)
    # calc seconds
    s = int(time - (SEC_IN_MIN * m))
    print(f'Вы ввели время в формате (чч:мм:сс): {h:02d}:{m:02d}:{s:02d}')


def task3():
    print("Задание №3")
    str_num = input("Введие число: ")
    num1 = int(str_num)
    num2 = int(str_num + str_num)
    num3 = int(str_num + str_num + str_num)
    sum_num = int(num1 + num2 + num3)
    print(f'Сумма {str_num}+{str_num}{str_num}+{str_num}{str_num}{str_num} = {sum_num}')


def task4():
    print("Задание №4")
    str_num = input("Введите целое положительное число: ")
    i = 0
    max_num = 0
    while i < len(str_num):
        if int(str_num[i]) > max_num:
            max_num = int(str_num[i])
        i = i + 1

    print(f'Максимальное число: {max_num}')


def task5():
    print("Задание №5")
    proceeds = int(input("Пожалуйста, введите сумму выручки вашей фирмы: "))
    costs = int(input("Пожалуйста, введите сумму издержек вашей фирмы: "))
    num_employees = int(input("Пожалуйста, введите количество сотрудников вашей фирмы: "))

    if proceeds > costs:
        profit = proceeds - costs
        print(f'Прибыль фирмы составила: {profit}')
        profitability = profit / proceeds
        print(f'Рентабельность выручки составила: {profitability:.2f}')
        revenue_employee = profit / num_employees
        print(f'Прибыль фирмы в расчете на одного сотрудника составила: {revenue_employee:.2f}')

        print(f'Фирма получила прибыль: {profit}')
    else:
        print("У фирмы убыток")


def task6():
    print("Задание №6")
    first_day_dist = int(input("Введите дистанцию первого дня: "))
    expected_day_dist = int(input("Введите ожидаемую дистанцию: "))
    nday_dist = first_day_dist
    nday = 1

    print("РЕЗУЛЬТАТ: ")
    while True:
        if nday_dist >= expected_day_dist:
            print(f'{nday}-й день: {nday_dist:.2f}')
            break

        print(f'{nday}-й день: {nday_dist:.2f}')

        nday_dist = nday_dist + 0.1 * nday_dist
        nday = nday + 1


task1()
task2()
task3()
task4()
task5()
task6()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
