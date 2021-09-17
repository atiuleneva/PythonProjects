def calc_1(a, b):
    print("Задание №1")
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        return "На ноль делить нельзя!"


a_num = int(input("Введите число: "))
b_num = int(input("Введите число: "))
print(calc_1(a_num, b_num))


def user_profile(**kwargs):
    print("Задание №2")
    print(kwargs)


user_profile(name="Ivan", lastname="Ivanov", birth_day=1993, city="Tula", email="ivanov@mail.ru", phone="+79102345678")


def my_func(a, b, c):
    print("Задание №3")
    return max([a+b, a+c, b+c])


a_num = int(input("Введите число: "))
b_num = int(input("Введите число: "))
c_num = int(input("Введите число: "))
print(my_func(a_num, b_num, c_num))


def my_pow(x, y):
    print("Задание №4")
    if y > 0:
        return "Функция возводит только в отрицательную степень!"
    res = x
    for num in range(-y-1):
        res = res * x

    return 1/res


x_num = float(input("Введите действительное положительное число: "))
y_num = int(input("Введите отрицательное число: "))
print(my_pow(x_num, y_num))


def sum_num(a):
    print("Задание №5")


print('Для выхода введите любой символ не цифры')
str_numbers = input("Введите несколько чисел через пробел: ")
str_list = str_numbers.split(" ")
total = 0
for n in str_list:
    total = total + int(n)
print(f'Сумма введеных чисел: {total}')

while True:
    global_num = input("Давайте посчитаем еще! Прибавим к полученному ответу еще несколько чисел. Введите новые числа "
                       "через "
                       "пробел: ")
    global_list = global_num.split(" ")
    try:
        for n in global_list:
            total = total + int(n)
    except ValueError:
        print(f'Сумма введеных чисел: {total}')
        print(f'Выход')
        break
    print(f'Сумма введеных чисел: {total}')


def up_func(a):
    return a.capitalize()
    # return a.title()


print("Задание №6")
str_up = input("Введите слово маленькими латинскими буквами: ")
print(up_func(str_up))

str_up = input("Введите предожение маленькими латинскими буквами: ")
str_list = str_up.split(" ")
i = 0
while i < len(str_list):
    str_list[i] = up_func(str_list[i])
    i = i + 1

print(" ".join(str_list))
