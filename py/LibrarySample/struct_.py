import struct
path = 'C:/Users/Tom/Documents/py/LibrarySample/a.bmp'
with open(path, 'rb') as f:
	s=f.read()
	print(s)
print(struct.unpack('<ccIIIIIIHH', s[0:30]))