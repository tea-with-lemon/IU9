"""������ 3

��� ���������� �� ���� �����:
- ������������(�������� �������) - ����������� ������ � ��������
- ������������
- �����������(��� ������������ ����� �� ������ ��������� ����, �� � �������������� �����-�� �����)"""

class Point:
	def __init__(self, x = 0.0,  y = 0.0, z = 0.0): ##�����������
		self.x = x
		self.y = y
		self.z = z
	def distance_to(self, point): ##���������� �� ������ �����
		return math.sqrt(
		(point.x - self.x)**2 +
		(point.y - self.y)**2 +
		(point.z - self.z)**2)
		
class Sphere(Point): ##�� Point
	def __init__(self, x = 0.0, y = 0.0, z = 0.0, r = 1.0)
		Point.__init__(self, x, y, z)
		self.r = r
	def area(self):
		return 4 * math.p * self.r**2
		
sph = Sphere(2.0, 2.0, 2.0, 1.0)
print((sph.area()) ##~12.6

class Figure:
	def __init__(self, sides):
		self.__sides = sides
	def scale(self, k):
		self.__sides = list(map (
			lambda x: x*k, 
			self.__sides))
	def sides(self):
		return self.__sides
	def area(self):
		raise NotImplementedError("���-��� ����� ��� �����������")

class Rectangle(Figure):
	def area(self):
		return ...
		
a = Figure([1, 2, 3])
b = a
b.scale(2)
print(a.sides()) ##[2, 4, 6]
print(b.sides()) ##[2, 4, 6]
	
import copy ## ���������� �������� ��� �����������
b = copy.copy(a) ##������������� �����������

copy.deepcopy() ##�������� ����� ��� ���������� �������� �������, �������� �����������
	
	
class Scene:
	def __init__(self, figures):
		self.__figures = figures
	def scale(self, k):
		for figure in self.__figures:
			figure.scale(k)
	def figures(self):
		return self.__figures
			
p = ([1, 2])
q = ([2, 3])
s1 = Scene([p, q])
s2 = copy.deepcopy(s1)
s2.scale(2)	
"""
##<= �������������� ��� ��� ������������ � �������������	

xs += [x] ##� �������� ��������� ����� ������
xs.append(x) ## ���������� �� �����
append + pop ##- ��������� ����.

xs.extend([1, 2])
[1, 2, 1, 3].count(1) => 2
			.index(1) => 0
			.sort()
			.reverse()"""
			
d = {1 : 'one', 2: 'two', 3: 'three'}
d.keys() #=> [1, 2, 3]
d.values() #=> ['one', 'two', 'three']
d.items() #=> [(1, 'one'), (2, 'two'), (3, 'three')]

d.has_key(0) #=> False

s.lower()
s.upper()
s.strip()
s.splut("1  2") #=> [1, 2]

s.isdigit()
s.isalpha()
.
.
.

s.format("...", arg1, arg2...)

f = open('file', 'r')
s = f.read()
f.close()

f.readline() ##����� ����� - ������ ������.
f.write(...)

d = {...}

def load_data(path):
	with open(path, "rt") as f:
		return eval(f.read())

def save_data(x, path):
	with open(path, "wt") as f:
		fwrite(repr(x)) ##repr - str
	
#������ pickle ��� ������������ � �������������� ������
#������ shelve ��� ��� ������

s = shelve.open(path)
s['hey'] = 'value'
x = s[k]
s.sync()
s.close()

import math #- ����������.