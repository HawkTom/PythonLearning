#----------类:class类名(object)-----
print('---------类:class类名(object)----------')
class Student(object):
	#__slots__=('__name','__score')
	def __init__(self,name='Tom',score=60):
		self.__name=name # __xx 外部不可直接访问变量
		self.__score=score
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	
	def print_score(self):
		print('%s:%s' % (self.__name,self.__score))
	def get_grade(self):
		if self.__score>=90:
			return 'A'
		elif self.__score>=60:
			return 'B'
		else:
			return 'C'
bart=Student('Bart Simpson',90)
setattr(bart,'x',1)
print(getattr(bart,'x',404))
print(bart.get_name())
bart.print_score()
print(bart.get_grade())
#print(dir(bart))

#---------类继承和多态--------------
print('---------类继承多态-----------')
class Animal(object):
	def run(self):
		print('Animal is runing')
class Cat(Animal):
	def run(self):
		print('Cat is runing')
cat=Cat()
cat.run()
class Timer(object):
	def run(self):
		print('Start...')
def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Timer())
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

