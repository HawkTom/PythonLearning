print('100+200+300 =', 100+200+300)
# name = input('Input your name: ')
name='Tom'
print('hello', name, '!')
print('I\'m \"python\",你好')
# ------------List-------------
L=[
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adem', 'Bart', 'Lisa'],
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
# -----------if-else----------
# birth =input('birth year: ')
birth = '1987'
if int(birth) > 2000:
	print('00后')
else:
	print('00前')
# ------------for-------------
for names in L[0]:
	print(names)
sum1 = 0
for x in range(101):
	sum1 = sum1+x
print(sum)
# ---------dict-----------
d={'Tom': 95, 'Bob': 85, 'Marry': 75}
d['Tom']
# ---------def----------
import math


def quadratic(a, b, c):
	x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
	return x1, x2
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


def power(x, n=2):
	s = 1
	while n > 0:
		n = n-1
		s=s*x
	return s
print(power(2))


def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
enroll('Tom','F',city='Shanghai')


def add_end(L=None):
	if L is None:
		L=[]
	L.append('end')
	return L
S=add_end()
S=add_end()
print(S)
def calc(*numbers):
	sum=0
	for n in numbers:
		sum = sum+n*n
	return sum
print(calc(*[1,2]))

def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
print(person('Tom',30,city='Beijing'))
extra={'city':'Hangzhou','gender':'Male'}
print(person('Marry',28,x=99,y=100))
#-------------递归调用--------------
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print(fact(5))
print(list(range(101))[3:50:5])








