"""
Урок 6. Работа с динамической памятью
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

Для примера беру Урок 2 задание 4:

4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
from memory_profiler import profile

n = 500
list = []

for i in range(0, n):
    list.append(i)
print(list)

@profile
def sum(n, list):
    result = 0
    if n <= len(list):
        for i in list[0:n]:
            result = result + i
        print(result)

sum(n, list)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    21     19.3 MiB     19.3 MiB           1   @profile
    22                                         def sum(n, list):
    23     19.3 MiB      0.0 MiB           1       result = 0
    24     19.3 MiB      0.0 MiB           1       if n <= len(list):
    25     19.3 MiB      0.0 MiB         501           for i in list[0:n]:
    26     19.3 MiB      0.0 MiB         500               result = result + i
    27     19.3 MiB      0.0 MiB           1           print(result)

"""

@profile
def recursion(list):
    def sumL(list,result,n):
        if n<0:
            return result
        else:
            return sumL(list,result+list[n],n-1)
    print(sumL(list,0,len(list)-1))

recursion(list)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    31     19.4 MiB     19.4 MiB           1   @profile
    32                                         def recursion(list):
    33     20.2 MiB      0.8 MiB         502       def sumL(list,result,n):
    34     20.2 MiB      0.0 MiB         501           if n<0:
    35     20.2 MiB      0.0 MiB           1               return result
    36                                                 else:
    37     20.2 MiB      0.0 MiB         500               return sumL(list,result+list[n],n-1)
    38     20.2 MiB      0.0 MiB           1       print(sumL(list,0,len(list)-1))
"""

"""
Вывод: рекурсия требует больше памяти
"""
