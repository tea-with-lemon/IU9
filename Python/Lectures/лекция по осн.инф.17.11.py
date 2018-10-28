# -*- coding: utf8 -*-
"""python.org
типизация строгая динамическая
python3 - linux, idle3
# -*- coding: utf8 -*-
Types:
    None
    Boolean (True, False == None, 0, (), []) operations: not, and, or
    ==  !=  <  >  <=  >=  in 
Arifmetic: **  %  /  %  (3+5j)-complex
Tuple 
  x= (int, "str")-число элементов постоянное, обращение по индексу 
  вложенные кортежи ((1,2,3), None)
  x,y,z=(1,2,3)
  print(x,y,z)
  len(x)
List
  xs=[1,2,3,4]
  len(xs)
  xs[-1]=2
  срезы
  xs[1:3] => [1,2]
  [:]
  xs.append(x)
  ys=xs+[35]
  xs[2:4]=[0,1]-добавление в середину
  t=[[1,2,3],[4,5,6]]
  t[0][1] =>2
  ex=[3,4,5]
  ex.append(7)
  ex.pop() =>7
  del ex[1]
String
  s= 'русский'
  len(s) =>7
  len(b'русский')-байтовая строка
  "string"
  "string 'string' string"
  '\'' "\""
  многострочные константы 
  x=1 '''line1
    line2
    line3'''
    
>>>ord('a')
97
>>>chr(48)
'0'
"abc"+"def"="abcdef"
1 in [1,2,2,3] => True
not (x in xs) == x not in xs
   >>>1 not in [1, 2, 3]
   False
print(int('123'))
float('1.5') => 1.5
str(12345) => '12345'
repr (1234) => '1234'
'abd'*7 => 'abdabdabdabdabdabdabd'
s[i:j:k]:
   >>>s='abdabdabdabdabdabdabd'
   >>>s[1:9:2]
   'badb'
max(s)-максимальный по коду символа
min(s)-минимальный по коду символа
>>>xs=[1,2,3]
>>>ys=xs.copy()
>>>ys
[1,2,3]
Sort
>>>xs=[4, 5, 7, 8, 1, 0, 2]
>>>xs.sort()
>>>xs
[0, 1, 2, 4, 5, 7, 8]
pr   s1=sorted(xs)
Dictionary
  d={key:'znachenie', 2:'two', 3:'three'}
  d={1:'one', 2:'two', 3:'three'}
  d[1] => one
  1 in d => True
  d.has.key(1) =>True
  d[1]='just one'
  list(d.keys())
  list(d.values())
  >>>d.keys()
  dict_keys([1, 2, 3])
https://wiki.python.org/moin/TimeComplexity
type(10) => int
>>>type('tre')==type(10)
False

Управляющие конструкции
if/elif/else"""

def my_abs(x):
    if x < 0:
        return -x
    else:
        return x
print(my_abs (-54))

def signum (x):
    if x < 0:
        return -1
    elif x==0:
        return 0
    else:
        return 1

for i in [1,2,3]:
    for j in range (10,30,10):
        print(i,j)
        #1 10
        #1 20
        #2 10
        #2 20
        #3 10
        #3 20
        
i=0
while i<5:
    i+=1
    print(i)
    
"""while | for
     if ...: continue
     if ...: break
   else:
     break выведет из программы 
pass-пустой блок"""


    

    
  



  



                               
  
