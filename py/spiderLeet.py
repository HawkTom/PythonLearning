
import urllib.request
from json import loads
import re
import pymysql

def getUrlList():
	req = urllib.request.Request ('https://leetcode.com/api/problems/all/')
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) '
								'AppleWebKit/537.36 (KHTML, like Gecko) '
								'Chrome/59.0.3071.115 Safari/537.36')
	# python3 默认取回bytes 需要decode（编码格式）将其转化为str格式
	html = urllib.request.urlopen(req).read().decode("utf-8")
	d = loads(html)
	return d['stat_status_pairs']

def getQuestionInfo(title):
	req = urllib.request.Request ('https://leetcode.com/problems/'+ title + '/')
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
								 'AppleWebKit/537.36 (KHTML, like Gecko) '
								 'Chrome/59.0.3071.115 Safari/537.36')
	html = urllib.request.urlopen(req).read().decode('utf-8')
	p = r'(?<=<meta name="description" content=")[\s\S]*?(?=" />)'
	result = re.search(p,html)
	if result:
		return result.group(0)
	else:
		return 'Error'

def formatQuestion(question_description):
	description = list(set(question_description.replace('\n ','\n').split('\n')))
	description.sort(key=question_description.index)
	return '\n'.join(description)

datas = getUrlList()
db = pymysql.connect("localhost","testuser","test123","leetcode")
c = db.cursor()
for data in datas[0:20]:
	title = data['stat']['question__title']
	Title = data['stat']['question__title_slug']
	Paid = data['paid_only']
	Question_ID = data['stat']['question_id']
	print(Question_ID)
	Difficulty_level = data['difficulty']['level']
	description = formatQuestion(getQuestionInfo(Title))
	sql = """INSERT INTO question (id, title, paid, difficulty, description) VALUE('%d','%s','%s','%d','%s') 
			 ON DUPLICATE KEY UPDATE title = '%s', paid = '%s', difficulty = '%d', description = '%s'"""\
		  % (Question_ID, title, Paid, Difficulty_level, description, title, Paid, Difficulty_level, description)
	c.execute(sql)
	db.commit()
db.close()
# print(x)
# print('Question ID:', data['stat']['question_id'])
# print('Difficulty level:', data['difficulty']['level'])
# print('Paid:', data['paid_only'])
# print('Title:', data['stat']['question__title'])
# print('Title slug:', data['stat']['question__title_slug'])