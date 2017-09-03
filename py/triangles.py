def triangles(max):
	L=[1]
	n=0
	while n<max:
		yield (L)
		L=[L[x]+L[x+1] for x in range(len(L)-1)]
		L.append(1)
		L.insert(0,1)
		n=n+1
	return 'done'

for n in triangles(10):
	print(n)



