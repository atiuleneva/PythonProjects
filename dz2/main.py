def task1():
    print("Задание №1")
    list_dz2 = ["hello", 57, 7, 'number', 3, 0, [0, 1, 2], ("23", 1, 5)]
    i = 0
    while i < len(list_dz2):
        print(f'Тип элемента {i}: {type(list_dz2[i])}')
        i = i + 1

    # for el in list_dz2:
    #     print(f'Тип элемента "{el}": {type(el)}')


def task2():
    print("Задание №2")
    user = input("Введите список чисел через пробел: ")
    user_list = user.split(" ")

    list_dz2 = []
    for n in user_list:
        list_dz2.append(int(n))
    print(f'Вы ввели список чисел: {list_dz2}')

    i = 0
    while i + 1 < len(list_dz2):
        el = list_dz2[i]
        list_dz2[i] = list_dz2[i+1]
        list_dz2[i+1] = el

        i = i + 2

    print(f'Результат перестановки: {list_dz2}')


def task3():
    print("Задание №3")
    user_month = int(input("Введите месяц года в ввиде целого числа: "))
    list_season = ["Зиме", "Зиме", "Весне", "Весне", "Весне", "Лету", "Лету", "Лету", "Осени", "Осени", "Осени", 'Зиме']
    print("list: ")
    print(f'Введенный месяц относитя к {list_season [user_month-1]}')

    user_dict = dict([(1, 'Зиме'), (2, 'Зиме'), (3, 'Весне'), (4, 'Весне'), (5, 'Весне'), (6, 'Лету'),
                      (7, 'Лету'), (8, 'Лету'), (9, 'Осени'), (10, 'Осени'), (11, 'Осени'), (12, 'Зиме')])
    print("dict: ")
    print(f'Введенный месяц относитя к {user_dict[user_month]}')


def task4():
    print("Задание №4")
    user_str = input("Введите строку со словами, введенными через пробел: ")
    user_list = user_str.split(" ")
    i = 0
    while i < len(user_list):
        print(f'{i+1} {user_list[i][0:10]}')
        i = i + 1


def task5():
    print("Задание №5")
    list_task_5 = [17, 13, 9, 9, 7, 7, 7, 6]
    print(f'Исходный список Рейтинга: {list_task_5}')
    user_num = int(input("Введите натуральное число: "))

    if user_num <= list_task_5[-1]:
        list_task_5.append(user_num)
        print(f'Введенное число {user_num} вставлено в конец списка: {list_task_5}')
    else:
        i = 0
        while i < len(list_task_5):
            if user_num > list_task_5[i]:
                list_task_5.insert(i, user_num)
                print(f'Введенное число занимает позицию {i} в {list_task_5}')
                break

            i = i + 1


# def task6():


task1()
task2()
task3()
task4()
task5()
# task6()



