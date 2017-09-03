import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use shal in python hashlib'.encode('utf-8'))
print(sha1.hexdigest())

db = {}


def get_md5(s):
	md5 = hashlib.md5()
	md5.update(s.encode('utf-8'))
	return md5.hexdigest()


def register(username, password):
	db[username] = get_md5(password + username + 'the_Salt')
	print('register success')


def login(user,password):
	if get_md5(password + user + 'the_Salt')==db[user]:
		print('Pass')
	else:
		print('Faild')

register('Tom','123456')
login('Tom','123456')