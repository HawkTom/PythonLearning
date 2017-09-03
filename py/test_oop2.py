#-----------@property---------------
class Screen(object):
	@property
	def width(self):
		return self.__width
	@width.setter
	def width(self,value):
		self.__width = value
	@property
	def height(self):
		return self.__height
	@width.setter
	def height(self,value):
		self.__height = value
	@property
	def resolution(self):
		return self.__height*self.__width
s=Screen()
s.width=1024
s.height=768
print(s.resolution)
#--------------定制类---------------
class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>100:
			raise StopIteration()
		return self.a
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
	def __str__(self):
		return 'Fib object' 
	def __getattr__(self,attr):
		if attr=='score':
			return 99
	def __call__(self):
		print('My name is %s' % self.a)
f=Fib()
for n in f:
	print(n)
print(f)
