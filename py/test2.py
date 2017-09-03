# -------返回函数-------
def lazy_sum(*args):
	def calc_sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return calc_sum
f=lazy_sum(1,3,5,7,9)
print(f())

# ----匿名函数lambda-----	
print(list(map(lambda x:x*x,[1,2,3,4,5])))

def build(x,y):
	return lambda: x*x+y*y
f1=build(1,2)
print(f1())

#--------装饰器-------
# def decorator(text):
	# def logo(func):
		# def wrapper(*args,**kw):
			# print('%s %s():' % (text,func.__name__))
			# ex=func(*args,**kw)
			# print('%s %s():' % (text,func.__name__))
			# return ex
		# return wrapper
	# return logo	
# @decorator('hw')
# def now():
    # print('2016-02-13: 1')
# now()


import functools
def log(arg):
    def decorator(func = arg):
        text = 'call' if func == arg else arg
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return (func(*args, **kw), print('end %s %s():' % (text, func.__name__)))[0]
        return wrapper
    return decorator() if callable(arg) else decorator
@log
def now():
    print('2016-02-13: 1')
now()
