"""
Урок 5.
Задание 7.

Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json


firm_list = []
firm_dict = {}
firm_profit = {}
firm_losses = {}
average_profit_dict = {}
profit = 0
sum_profit = 0
average_profit = 0
number_firms_profit = 0
number_firms_losses = 0

with open("text_les5-ex7.txt", encoding='UTF-8') as f:
    while True:
        read_line = f.readline()
        if not read_line:
            break
        else:
            read_list = list(read_line.split())
            firm_name = read_list[0]
            ownership_form = read_list[1]
            revenue = float(read_list[2])
            costs = float(read_list[3])
            profit = revenue - costs
            if profit >= 0:
                firm_profit.update({firm_name: profit})
                number_firms_profit += 1
                sum_profit += profit
            else:
                firm_losses.update({firm_name: profit})
                number_firms_losses += 1


average_profit = round(sum_profit / number_firms_profit, 2)
average_profit_dict.update({'average_profit': average_profit})

firm_list = [firm_profit, firm_losses, average_profit_dict]
# print(firm_list)

firm_dict = {'firm_profit': firm_profit, 'firm_losses': firm_losses, 'average_profit_dict': average_profit_dict}
# print(firm_dict)

with open("json_list_les5-ex7.json", 'w') as fw_list_json:
    json.dump(firm_list, fw_list_json)

with open("json_dict_les5-ex7.json", 'w') as fw_dict_json:
    json.dump(firm_dict, fw_dict_json)

with open("json_list_les5-ex7.json") as fr_list_json:
    data_1 = json.load(fr_list_json)

print(data_1)
print(type(data_1))

with open("json_dict_les5-ex7.json") as fr_dict_json:
    data_2 = json.load(fr_dict_json)

print(data_2)
print(type(data_2))
