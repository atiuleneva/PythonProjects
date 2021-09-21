import sys
from functools import reduce
import itertools


def search_sequence(num_list):
    print("Задание №2")
    prev_item = sys.maxsize
    for num in num_list:
        if prev_item < num:
            yield num
        prev_item = num


global_num_list = [300, 3, 12, 4, 4, 44, 50, 10, 33, 1, 22]
result = list(search_sequence(global_num_list))
print(result)


def multiples():
    print("Задание №3")
    _multiples = list(el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0)
    print(_multiples)


multiples()

print("Задание №4")
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list_2 = [i for i in my_list if my_list.count(i) < 2]
print(my_list_2)


def my_func(prev_el, el):
    return prev_el * el


print("Задание №5")
my_list5 = list(el for el in range(99, 1001) if el % 2 == 0)
print(my_list5)
print(reduce(my_func, my_list5))


print("Задание №6")
print("6.1 ======================")
for i in itertools.count(3, 3):
    if i >= 10:
        break
    print(i)
# gen = itertools.count(3, 2)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

print("6.2 ======================")
count = 0
for i in itertools.cycle([1, 3, 5, 7, 9]):
    if count > 9:
        break
    count += 1
    print(i)


def gen_7(n):
    print("Задание №7")
    num_f = 1
    for element in range(1, n+1):
        num_f = num_f * element
        yield num_f


for el in gen_7(5):
    print(el)








