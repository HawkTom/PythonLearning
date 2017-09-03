import itertools
natuals = itertools.count(1)
nn = itertools.takewhile(lambda x:x <= 10,natuals)
cs = itertools.cycle('ABC')
ns = itertools.repeat('A', 3)
for n in nn:
	print(n)
for c in itertools.chain('ABC','XYZ'):
	print(c)