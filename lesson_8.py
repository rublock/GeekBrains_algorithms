"""
Урок 8. Деревья. Хэш-функция
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib

def substr(str):
    h_lst = []
    s_lst = []

    for i in range(1, len(str)):
        for j in range(len(str) - i + 1):
            h_sub = hashlib.sha1(str[j:j + i].encode('utf-8')).hexdigest()
            if h_sub not in h_lst:
                h_lst.append(h_sub)
                s_lst.append(str[j:j + i])

    if len(s_lst) > 0:
        return f'В строке "{str}" найдено {len(s_lst)} уникальные подстроки: \n{s_lst}'

print(substr('wikipedia'))

"""2. Закодируйте любую строку из трех слов по алгоритму Хаффмана."""
from collections import deque

str = 'beep boop beer!'
dict = {}
codes = {}
result = ''

"""отсортировываю по повторам символов в троке"""
for c in str:
    if c not in dict:
        dict[c] = str.count(c)
sorted_dict = deque(sorted(dict.items(), key=lambda item: item[1]))
print(sorted_dict)

"""строю дерево элементов в виде словаря"""
def tree(sorted_dict):
    if len(sorted_dict) != 1:
        while len(sorted_dict) > 1:
            weight = sorted_dict[0][1] + sorted_dict[1][1]
            comb = {0: sorted_dict.popleft()[0],
                    1: sorted_dict.popleft()[0]}
            for i, _count in enumerate(sorted_dict):
                if weight > _count[1]:
                    continue
                else:
                    sorted_dict.insert(i, (comb, weight))
                    break
            else:
                sorted_dict.append((comb, weight))
    else:
        weight = sorted_dict[0][1]
        comb = {0: sorted_dict.popleft()[0], 1: None}
        sorted_dict.append((comb, weight))
    print(sorted_dict[0][0])
    return sorted_dict[0][0]

"""рекурсивно добавляю коды к каждому символу"""
def code(tree, path=''):
    if not isinstance(tree, type(dict)):
        codes[tree] = path
    else:
        code(tree[0], path=f'{path}0')
        code(tree[1], path=f'{path}1')

code(tree(sorted_dict))

print(codes)

for i in str:
    result += codes[i] + ' '

print(f'{str} = {result}')