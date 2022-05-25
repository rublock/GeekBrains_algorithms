# Урок 3. Массивы. Кортежи. Множества. Списки.

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
print('ЗАДАНИЕ 1.')
list = []
count = 0
for i in range(2, 100):
    list.append(i)
print(list)

for j in range(2, 100):
    for y in range(len(list)):
        if list[y] % j == 0:
            count += 1
    print(f'{j} кратно {count} цифр в диапазоне от 2 до 99')
    count = 0

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
list = [8, 3, 15, 6, 4, 2]
print(f'ЗАДАНИЕ 2.\nДан массив {list}')
list2 = []
count = 0
for i in list:
    count += 1
    if i % 2 == 0:
        list2.append(count)
print(f'Индексы четных элементов первого массива {list2}')

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
list = []
for i in range(10):
    list.append(random.randrange(1,99))
print(f'ЗАДАНИЕ 3.\nДан массив: \n{list}')

max = list[0]
for ele in list:
    if ele > max:
       max = ele

min = list[0]
for ele in list:
    if ele < min:
       min = ele

list[list.index(min)], list[list.index(max)] = list[list.index(max)], list[list.index(min)]
print(f'Массив где минимальный и максимальный элементы поменяны местами: \n{list}')

# 4. Определить, какое число в массиве встречается чаще всего.
list = [1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6]
print(f'ЗАДАНИЕ 4.\nДан массив {list}')

count_1 = 0
count_2 = 0

for i in range(len(list)):
    for j in list:
        if list[i] == j:
            count_1 += 1
    if count_1 > count_2:
        result = f'Цифра {list[i]} встречается {count_1} раза'
        count_2 = count_1
    count_1 = 0
print(result)

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
list = [1, 2, -6, 2, 3, -3, 9]
print(f'ЗАДАНИЕ 5.\nДан массив {list}')
result = 0
temp = 0

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[j] < list[i]:
            temp = list[j]
            if temp < result:
                result = temp
                print(f'Минимальный элемент массива {result} на позиции {j + 1}')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и
# максимальный элементы в сумму не включать.
list = [1, 2, -6, 2, 3, -3, 9]
print(f'ЗАДАНИЕ 6.\nДан массив {list}')
result = 0
temp = 0
position_1 = 0
position_2 = 0
sum = 0

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[j] < list[i]:
            temp = list[j]
            if temp < result:
                result = temp
                position_1 = j + 1
                print(f'Минимальный элемент {temp} на позиции {j + 1}')

for y in range(len(list)):
    for k in range(y + 1, len(list)):
        if list[k] > list[y]:
            temp = list[j]
            if temp > result:
                result = temp
position_2 = k
print(f'Максимальный элемент {result} на позиции {k + 1}')

for n in list[position_1:position_2]:
    sum += n
print(f'Cумма элементов, находящихся между минимальным и максимальным элементами = {sum}')

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
list = [1, 2, -6, 2, 3, -3, 9]
print(f'ЗАДАНИЕ 7.\nДан массив {list}')
result = 0
temp = 0

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[j] < list[i]:
            temp = list[j]
            if temp < result:
                result = temp
print(f'Первый наименьший элемент {result}')
list.remove(result)
result = 0

for k in range(len(list)):
    for n in range(k + 1, len(list)):
        if list[n] < list[k]:
            temp = list[n]
            if temp < result:
                result = temp
print(f'Второй наименьший элемент {result}')

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов
# каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
print('ЗАДАНИЕ 8.')
list_1 = []
result = ''
for i in range(4):
    list_2 = []
    sum = 0
    for j in range(5):
        r = int(input('Введите число: '))
        list_2.append(r)
        sum += r
    list_1.append(list_2)
    print(f'{list_2} | {sum}')
    result += f'{list_2} | {sum}\n'
print(result)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
print('ЗАДАНИЕ 9.')
list_1 = []
for i in range(5):
    list_2 = []
    for j in range(5):
        r = random.randrange(0,99)
        list_2.append(r)
    list_1.append(list_2)
    print(list_2)

count = 0
x = 1
list_min = []
for z in range(len(list_1)):
    num = 99
    temp = 0
    for y in range(len(list_1)):
        for n in range(x, len(list_1)):
            result1 = list_1[y][count]
            result2 = list_1[n][count]
            if result1 < result2:
                temp = result1
                if temp < num:
                    num = temp
        x = 0
    list_min.append(num)
    count += 1
print('_' * 20)
print(list_min)

result = 99
for c in range(len(list_min)):
    for v in range(c + 1, len(list_min)):
        if list_min[v] < list_min[c]:
            temp2 = list_min[v]
            if temp2 < result:
                result = temp2
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы {result}')