# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import random

data = input('Введите трехзначное число: ')
print(int(data[0]) + int(data[1]) + int(data[2]))

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.
a = 5
b = 6
print(bin(a)) #0b101
print(bin(b)) #0b110
print(bin(a | b)) #0b111  #Бинарный оператор | копирует бит, если тот присутствует в хотябы одном оперднде.
print(bin(a>>2)) #0b1     #Бинарный оператор >> сдвигает значение левого операнда право на количество бит указанных в правом операнде.
print(bin(a<<2)) #0b10100 #Бинарный оператор << сдвигает значение левого операнда влево на количество бит указанных в правом операнде.

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
x1 = float(input('Введите координаты x1: '))
x2 = float(input('Введите координаты x2: '))
y1 = float(input('Введите координаты y1: '))
y2 = float(input('Введите координаты y2: '))
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(f'Уравнение прямой y = {round(k,2)}x + {round(b, 2)}')

# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
# случайное целое число;
start_int = input('Введите начало диопазона целых чилел: ')
end_int = input('Введите конец диопазона целых чилел: ')
print(random.randint(int(start_int), int(end_int)))

# случайное вещественное число;
import random
start_float = int(float(input('Введите начало диопазона вещественных чилел: ')))
end_float = int(float(input('Введите конец диопазона вещественных чилел: ')))
print(random.uniform(start_float, end_float))

# случайный символ.
import random
start_letter = input(str('Введите начало диопазона букв в алфавите: '))
end_letter = input(str('Введите конец диопазона букв в алфавите: '))
print(chr(random.randint(ord(start_letter), ord(end_letter))))

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
data = input('Введите две буквы через пробел: ').split()
count_1 = 0
count_2 = 0
import string
for i in string.ascii_lowercase:
    count_1 += 1
    if i == data[0]:
        print(f'Номер первой введенной буквы: {count_1}')
        count_2 = count_1
    elif i == data[1]:
        print(f'Номер второй введенной буквы: {count_1}')
        break
print(f'Расстояние между буквами {count_1 - count_2}')

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string
num = int(input('Введите номер буквы: '))
my_list = list(string.ascii_lowercase)
print(my_list[num - 1])





