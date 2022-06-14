"""
Урок 7. Алгоритмы сортировки
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint
from timeit import timeit

list = [randint(-100, 100) for i in range(10)]
print(list)

def buble_sort(list, count=1):
    while count < len(list):
        for i in range(len(list) - count):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        count += 1
    return list

print(buble_sort(list))
print(timeit('buble_sort(list[:])', globals = globals(), number=1000))

"""лучшаем сортировку, разбивкой списка на 2 части"""
def upgraded_buble_sort(list, left=0):
    right = len(list) - 1
    while left <= right:
        for i in range(left, right):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        right -= 1
        for i in range(right, left, -1):
            if list[i - 1] > list[i]:
                list[i], list[i - 1] = list[i - 1], list[i]
        left += 1
    return list

print(upgraded_buble_sort(list[:]))
print(timeit('upgraded_buble_sort(list[:])', globals = globals(), number=1000))

"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
"""
from random import randint

list = [randint(0, 50) for i in range(10)]
print(list)

def merge(left_list, right_list):
    result = []
    l = 0
    r = 0

    for i in range(len(left_list) + len(right_list)):
        if l < len(left_list) and r < len(right_list):

            if left_list[l] <= right_list[r]:
                result.append(left_list[l])
                l += 1

            else:
                result.append(right_list[r])
                r += 1

        elif l == len(left_list):
            result.append(right_list[r])
            r += 1

        elif r == len(right_list):
            result.append(left_list[l])
            l += 1

    return result

def middle_list(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2

    left_list = middle_list(list[:mid])
    right_list = middle_list(list[mid:])

    return merge(left_list, right_list)

print(middle_list(list))

"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, 
делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без 
сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
from random import randint
import math

m = 10
list = [randint(0, 50) for i in range(2 * m + 1)]
print(list)

"""для сортировки списка, беру за основу сортировку Шелла"""
def shellSort(list):
    n = len(list)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = list[i]
            j = i
            while j >= interval and list[j - interval] > temp:
                list[j] = list[j - interval]
                j -= interval
            list[j] = temp
        k -= 1
        interval = 2**k -1
    return list

result = shellSort(list)
print(result)
print(f'Медиана = {result[m]}')