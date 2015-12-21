# -*- coding: utf8 -*-
def gcd(m,n):
    while n:
        m,n=n, m%n
    return abs(m)
m,n=int(input()), int(input())
print(gcd(m,n))

""" global- переменная, которая может изменяться в функции
t1=gcd(n=9,m=6)

def f(x=0):
    .
    .
    .
f(1)
f() == f(0)"""
def f(*args):
    print('Число аргументов:', len(args))
    print (args)
f(1,2,3)

def g(**args):
    print (args)

g(first=1, second=2)
#{'first':1,'second':2}

"""def h(*args, **kvargs): f(1,2,3)
.
.
.
def h(x, *arg, **kvargs)
h(    1  (2,3)  {'fourth':4})-подстановка при вызове h(1,2,3,fourth=4)"""

list(map(abs, [-1,-2,-3]))
list(filter(lambda x: x % 2 == 0, [1,2,3,4,5]))
reduce(lambda x,y: x+y, [1,2,3])
#второй аргумент функции sorted посмотреть
"""ys=sorted(xs)
xs.sort()

def f(x):........ == f=lambda x:.......


List comprehension
генерация списка по условию
списковые выражения
[x**2 for x in range(10,100) if x%2 == 0]


apply()
Функция для применения другой функции к позиционным и именованным аргументам, 
заданным списком и словарем соответственно (Python 2):

>>> def f(x, y, z, a=None, b=None):
...     print x, y, z, a, b
...
>>> apply(f, [1, 2, 3], {'a': 4, 'b': 5})
1 2 3 4 5
В Python 3 вместо функции apply() следует использовать специальный синтаксис:

>>> def f(x, y, z, a=None, b=None):
...     print(x, y, z, a, b)
...
>>> f(*[1, 2, 3], **{'a': 4, 'b': 5})
1 2 3 4 5"""
from functools import*
reduce(lambda x,y: x+y, [1,2,3])
"""@t  #декоратор
def f(...):
    .
    .
    .
   эквивалентно
def f(...):
    .
    .
    .
f=t(f)

def x10(fn):
    return (lambda: *args1, **args2:
            fn(*args1, *args2) *10)
@x10
def rec(x): return 1.0/x
y=rec(2)
"""
#ООП
"""class Point:
    x=0.0
    y=0.0
    z=0.0
p=Point()
p.x => 0.0
p.x =  1.0
p.x => 1.0


class Point:
    pass
p=Point()
p.x=1.0
p.x => 1.0

ООП - парадигма программирования, в которой основными концепциями явялются понятия объектов
Класс(class) - абстрактный тип данных, объединяющий поля данных и методы их обработки
Позволяет иметь много объектов с одинаковым свойством и поведением
Объект(object) - воплощение какого-то класса (экземпляр)
Члены класса (class members, поля)
     /                              \
 атрибуты                         методы
(свойства)                       возвращают или изменяют состояние объекта
поля класса
хранят состояние объекта

del - удаляет отдельные элементы """

class Point:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x=x
        self.y=y
        self.z=z
    def distance_to(self, point):
        return math.sqrt(point.x-self.x)**2 + (point.y-self.y)**2 + (point.z-self.z)**2
    
a=Point(0.0,1.0,0.0)
o=Point
a.distance_to(o)
    