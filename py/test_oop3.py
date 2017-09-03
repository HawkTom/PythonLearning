#------------枚举类Enum--------------
from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr'))
print(Month(2).name)
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
#----------元类type----------------
#-----------错误处理-------------
try:
	print('try...')
	r=10/5
	print('result:',r)
except ZeroDivisionError as e:
	print('except',e)
else:
	print('no error')
finally:
	print('finally')
print('END')