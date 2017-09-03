d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
# -------file IO---------------
with open('C:/Users/Tom/Documents/py/123.txt', 'w') as f:
	f.write('hello world')
with open('C:\\Users\\Tom\\Documents\\py\\123.txt', 'r') as f:
	print(f.read())
# -------StringIO-------------------
from io import StringIO
f = StringIO()
f.write('hello world String IO')
print(f.getvalue())  # getvalue()获得写入后的str
# --------BytesIO-------------
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# ----------------
print('----------------')
import os
path = 'C:/Users/Tom/Documents/py'
print(os.listdir(path))
print([s for s in os.listdir(path) if os.path.isdir(os.path.join(path, s))])
