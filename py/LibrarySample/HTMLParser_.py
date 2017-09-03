# ----这个着实看不懂------
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLPaser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)

	def handle_endtag(self, tag):
		print('<%s>' % tag)

	def handle_startendtag(self, tag, attrs):
		print('<%s>' % tag)

	def handle_data(self, data):
		print(data)

	def handle_comment(self, data):
		print('<!--', data, '-->')

	def handle_entityref(self, name):
		print('&%s;' % name)

	def handle_charref(self, name):
		print('&#%s;' % name)

pasrser = MyHTMLPaser()
with open('C:/Users/Tom/Documents/py/LibrarySample/123.txt', 'r') as f:
	html = f.read()
with open('C:/Users/Tom/Documents/py/LibrarySample/234.txt', 'w') as f:
	f.write(str(pasrser.feed(html)))
