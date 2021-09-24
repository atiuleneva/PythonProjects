import json

print("Task #1")
f_1 = open("dz_file_1.txt", 'w')
while True:
    user_inp = input("Введите строку: ")
    f_1.write(user_inp + "\n")
    if not user_inp:
        break

f_1.close()

print("Task #2")
f_2 = open("dz_file_2.txt")
f_2_lines = f_2.readlines()
print(f'Количество строк в файле dz_file_2 = {len(f_2_lines)}')
for i in range(0, len(f_2_lines)):
    word_list = f_2_lines[i].split()
    print(f'Количество слов в строке {i+1}: {len(word_list)} ')

f_2.close()

print("Task #3")
f_3 = open("dz_file_3.txt")
f_3_lines = f_3.readlines()
payroll = {}
for line in f_3_lines:
    surname, salary = line.rstrip("\n").split(" ")
    payroll[surname] = int(salary)

print(payroll)
low_salary = list(key for key in payroll if payroll[key] < 20000)
print("Список сотрудников с зарплатой менее 20000 руб: ")
for el in low_salary:
    print(f'{el}: {payroll[el]}')

total = 0
for key in payroll:
    total = payroll[key] + total

print(f'Средняя заработная плата сотрудников = {round(total/len(payroll))}')

f_3.close()

print("Task #4")
f_4 = open("dz_file_4.txt")
f_4_new = open("dz_file_4_new.txt", 'w', encoding="utf-8")
f_4_lines = f_4.readlines()
num_dict = {}
for line in f_4_lines:
    text_num, num = line.rstrip("\n").split(" - ")
    num_dict[text_num] = int(num)


print(num_dict)
ru_text_num = dict(One='Один', Two='Два', Three='Три', Four='Четыре')
for key in num_dict:
    f_4_new.writelines(f'{ru_text_num[key]} - {num_dict[key]}\n')

f_4.close()

print("Task #5")
f_5 = open("dz_file_5.txt", 'w', encoding="utf-8")
num_list = ['2', '3', '4', '7', '10']
sum_num = 0
for el in num_list:
    sum_num = int(el) + sum_num

# print(num_list)
print(f'Набор чисел: {" ".join(num_list)}', file=f_5)
print(f'Сумма чисел = {sum_num}')

f_5.close()

print("Task #6")
f_6 = open("dz_file_6.txt", encoding="utf-8")
f_6_lines = f_6.readlines()
education = {}
for line in f_6_lines:
    subject, lecture, pract, lab = line.rstrip("\n").split(" ")
    education[subject] = int(lecture) + int(pract) + int(lab)

print(education)

f_6.close()

print("Task #7")
f_7 = open("dz_file_7.txt")
f_7_lines = f_7.readlines()
firm_info_list = []
fin_result_dict = {}
sum_profit_firms = 0
num_profit_firms = 0
for line in f_7_lines:
    firm, prop, proceeds, costs = line.rstrip("\n").split(" ")
    fin_result_dict[firm] = int(proceeds) - int(costs)
    if fin_result_dict[firm] > 0:
        sum_profit_firms = sum_profit_firms + fin_result_dict[firm]
        num_profit_firms += 1

avg_dict = {"average_profit": sum_profit_firms/num_profit_firms}

firm_info_list.append(fin_result_dict)
firm_info_list.append(avg_dict)

print(firm_info_list)

with open("dz_file_7.json", "w") as f_7_json:
    json.dump(firm_info_list, f_7_json)

f_7.close()
































