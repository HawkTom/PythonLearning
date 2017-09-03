import re
result1 = re.match(r'^\d{3}\-\d{3,8}$','010-123a45')
result = re.match(r'^(<[0-9a-zA-Z\s]+>)\s([0-9a-zA-Z]+@[0-9a-zA-Z]+.[a-z]+)$','<Tom Paris> tom@voyager.org')

with open(r'C:/Users/Tom/Documents/py/123.txt', 'r',encoding='utf-8') as f:
	data = f.read()
	data = data.replace('\n ','\n')
	# print(data)
	data = data.split('\n')
	# print(data)
	data1 = list(set(data))
	data1.sort(key = data.index)
	data1.remove('')
	print('\n'.join(data1))
	# print('\n'.join(data1))
	# p = r'(?<=<meta name="description" content=")[\s\S]*?(?=" />)'
	# result2 = re.search(p,data)
	# if result2:
	# 	print('OK')
	# 	print(result2.group(0))
	# else:
	# 	print('Faild')

