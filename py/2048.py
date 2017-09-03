import msvcrt, os
import random

def GetKey():
	ch = msvcrt.getch()
	ListKeys =[b'w', b's', b'a', b'd']
	while ch not in ListKeys:
		ch = msvcrt.getch()
	return ListKeys.index(ch)
	
def PrtMap(map):
	os.system('CLS')
	for Line in map:
		for Block in Line:
			print (Block, end='\t')
		print()


def mov(map, fx):
	if fx == 3: #right
		for y in range(4):
			for x in range(3):
				if map[y][x+1] == 0 and map[y][x] !=0:
					map[y][x+1] = map[y][x]
					map[y][x] = 0
				if map[y][x+1] == map[y][x]:
					map[y][x+1] *= 2
					map[y][x] = 0
	if fx == 2: #left
		for y in range(4):
			for x in range(3, 0, -1):
				if map[y][x-1] == 0 and map[y][x] !=0:
					map[y][x-1] = map[y][x]
					map[y][x] = 0
				if map[y][x-1] == map[y][x]:
					map[y][x-1] *= 2
					map[y][x] = 0
	if fx == 1: #down
		for y in range(3):
			for x in range(4):
				if map[y+1][x] == 0 and map[y][x] !=0:
					map[y+1][x] = map[y][x]
					map[y][x] = 0
				if map[y+1][x] == map[y][x]:
					map[y+1][x] *= 2
					map[y][x] = 0
	if fx == 0: #up
		for y in range(3, 0, -1):
			for x in range(4):
				if map[y-1][x] == 0 and map[y][x] !=0:
					map[y-1][x] = map[y][x]
					map[y][x] = 0
				if map[y-1][x] == map[y][x]:
					map[y-1][x] *= 2
					map[y][x] = 0
	return map

def New(map):
	#2 or 4
	x, y = random.randint(0, 3), random.randint(0, 3)
	while map[y][x] !=0:
		x, y = random.randint(0, 3), random.randint(0, 3)
	map [y][x] = 2*random.randint(1, 2)
	return map
	
map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PrtMap(map)
while True:
	key = GetKey()
	map = mov(map, key)
	map = New(map)
	PrtMap(map)


