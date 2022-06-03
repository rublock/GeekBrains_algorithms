# Урок 4. Эмпирическая оценка алгоритмов на Python

# ЗАДАНИЕ 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

#для примера использовал ЗАДАНИЕ 1 из УРОКА 3 В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
print('ЗАДАНИЕ 1.')
import cProfile
def main(list = [], count = 0):
    for i in range(2, 1000000):
        list.append(i)

    for j in range(2, 10000000):
        for y in range(len(list)):
            if list[y] % j == 0:
                count += 1
        return f'{j} кратно {count} цифр в диапазоне от 2 до 99'
        count = 0

cProfile.run('main()') #1000003 function calls in 0.263 seconds

# Оптимизация, создаем массив с использованием lambda функции
import cProfile
def main(count = 0):
    list = [i for i in range(2, 1000000)]

    for j in range(2, 10000000):
        for y in range(len(list)):
            if list[y] % j == 0:
                count += 1
        return f'{j} кратно {count} цифр в диапазоне от 2 до 99'
        count = 0

cProfile.run('main()') #6 function calls in 0.157 seconds

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
print('ЗАДАНИЕ 2.')
import timeit
import cProfile
# n = int(input('Введите число до 5: '))
def prime(n):
    list = []
    for i in range(1, 1000000):
        list.append(i)

    list[1] = 0

    def is_prime(i):
        if i % 2 == 0:
            return i == 2
        d = 3
        while d * d <= i and i % d != 0:
            d += 2
        return d * d > i

    count = 0
    for i in list:
        if is_prime(i) == True:
            count += 1
            if count == n:
                return f'{n}е простое по счету число = {i}'

print(timeit.timeit(lambda: print(prime(100)), number = 1))
cProfile.run('prime(100)')

# с использованием решета Эратосфена
def eratosthenes(n):
    my_list = list(range(1000000 + 1))
    my_list[1] = 0
    for i in my_list:
        if i > 1:
            for j in range(i + i, len(my_list), i):
                my_list[j] = 0
    sieve1 = [x for x in my_list if x != 0]
    return f'{n}е простое по счету простое число = {sieve1[n - 1]}'

print(timeit.timeit(lambda: print(eratosthenes(100)), number = 1))
cProfile.run('eratosthenes(100)')