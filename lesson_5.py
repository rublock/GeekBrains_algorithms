# Урок 5. Коллекции. Список. Очередь. Словарь.

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

dict = {}
number_of_factories = int(input('Введите количество предприятий: '))

for i in range(number_of_factories):
    names_of_factories = input(f'Введите название {i + 1} предприятия: ')
    earnings_of_factories = int(input(f'Введите прибыль {i + 1} предприятия: '))
    dict[names_of_factories] = earnings_of_factories

print(dict)

class AverageProfit:
    def __init__(self, dict):
        self.dict = dict

    def average_profit_all(self):
        average = float(sum(dict.values())) / len(dict)
        return average

    def winners(self, avg):
        loosers_list = []
        for i in self.dict:
            if dict[i] > avg:
                loosers_list.append(i)
        return loosers_list

    def loosers(self, avg):
        loosers_list = []
        for i in self.dict:
            if dict[i] < avg:
                loosers_list.append(i)
        return loosers_list

run = AverageProfit(dict)
avg = run.average_profit_all()
print(f'Средняя прибыль всех предприятий {avg}')
print(f'Предприятия с прибылью выше среднего {run.winners(avg)}')
print(f'Предприятия с прибылью ниже среднего {run.loosers(avg)}')

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

first_number = list(input('Введите первое число в шестнадцатеричном формате: '))
second_number = list(input('Введите второе число в шестнадцатеричном формате: '))

sum = list(hex(int(''.join(first_number), 16) + int(''.join(second_number), 16)))
mul = list(hex(int(''.join(first_number), 16) * int(''.join(second_number), 16)))

for i in range(1, len(sum)):
    sum[i] = sum[i].upper()
print(f'Сумма чисел {sum[2:]}')

for i in range(1, len(mul)):
    mul[i] = mul[i].upper()
print(f'Произведение чисел{mul[2:]}')