import base64
new = base64.b64encode(b'binary\x00string')
print(new)
old = base64.b64decode(new)
print(old)
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))


def safe_base64_decode(s):
	return s.decode().strip('=')

print(safe_base64_decode(new))
