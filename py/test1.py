#---------------reduce和map
from functools import reduce
def add(x,y):
	return x*10+y

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5}[s]

r = reduce(add,map(char2num,'14352'))
print(r)

def normalize(name):
	return str.capitalize(name)
	
print(list(map(normalize,['adam','LISA','barT'])))

def prod(L):
	def multi(x,y):
		return x*y
	return reduce(multi,L)
print('1*3*5*7=',prod([1,3,5,7]))


def str2float(s):	
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}[s]
	def num2float(x,y):
		if isinstance(y,str):
			return x
		else:
			return x*10+y
	return reduce(num2float,map(char2num,s))/(10**(len(s)-s.index('.')-1))
print(str2float('12388.45678'))
			
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n
def _not_divisible(n):
	return lambda x: x%n>0
# ------过滤序列filter-----
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n=next(it)
		yield n
		it = filter(_not_divisible(n),it)
for n in primes():
	if n<20:
		print(n)
	else:
		break
		
def is_palindrome(num):
	return str(num)==str(num)[::-1]
print(list(filter(is_palindrome,range(1,1000))))

L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
	




