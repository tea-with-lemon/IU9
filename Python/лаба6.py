# -*- coding: utf8 -*-
#1 задание циклом
def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

def gcd(a, b):
    a,b=abs(a),abs(b)
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return abs(a)


#рекурсией

def rec_gcd(x,y):
    x,y=abs(x),abs(y)
    if (y == 0):
        return x
    return rec_gcd(y, x%y)

def rec_lcm(x,y):
    return abs(x//rec_gcd(x,y))*y  

#2 задача
"""Напишите программу, которая в диалоговом режиме запрашивает у пользователя ввод чисел и запоминает их. Ввод пользователем пустой строки означает окончание ввода. По окончании ввода программа вычисляет и выводит в консоль:

-количество введенных чисел,
-сумму введенных чисел,
-среднее арифметическое этих чисел,
-наибольшее из введенных чисел,
-наименьшее из введенных чисел,
-число, квадратный корень которого является наименьшим в ряду квадратных корней введенных чисел,
-число, квадратный корень которого является наибольшим в ряду квадратных корней введенных чисел.
"""


xs=list(map(float, input().split()))
print(len(xs))
print(sum(xs))
print(sum(xs)/len(xs))
print(max(xs))
print(min(xs))
ys=min([x**2 for x in xs])
zs=max([x**2 for x in xs])

#3 задача
import collections 

def how_many(s):
    d = dict()
    for c in s:
        if c.isalpha():
            c=c.lower()
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return collections.OrderedDict(sorted(d.items()))
#s=str(input())
#for k, v in how_many(s).items():
#    print(k, v)

#4 задача
from random import randint

def random_sample(xs, k):
    xs=[2, 4, 0, 7, 9, 5]
    ys = []
    n = len(xs)
    for i in range(xs[0],xs[n-1]):
        ys.append(i)
    print(ys)
xs = [2, 4, 0, 7, 9, 5]
k = int(input())
random_sample(xs,k)
     
# задача 5
from itertools import product

alphabet = input().split()
r = int(input())

def permutations(str, r, repl):
    for indices in product(range(len(str)), repeat=r):
        res = []
        for i in indices:
            res.append(str[i])
        if repl==1:
            flag = 0
            for i in range(len(indices)-1):
                if indices[i] in indices[i+1:]:
                    flag = 1
                    break
            if flag == 1:
                continue
        print(res)
        
permutations(alphabet, r, 1)
