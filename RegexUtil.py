import re
class RegexUtil:
	@staticmethod
	def findWords(text,minLength=1):
		m = re.findall('\w{' + minLength + ',}',text)
		return m

	def findLinks(text):
		m = re.findall('\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))',text)
		return m

	def matchArabic(text):
		m = re.findall('([\u0621-\u0670]+)',text)
		return m

	def findControlChars(text):
		m = re.findall('(?![\u000d\u000a\u0009])\p{C}')
		return m

	def twitterNames(text):
		m = re.findall('@\w{1,15}')
		return m

	def hashtags(text):
		m = re.findall('#\w+')
		return m

	def findEmails(text):
		m = re.findall('[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?',text)
		return m

	def findNumbers(text):
		m = re.findall('\d+',text)
		return m

	def removeExtraSpaces(text):
		return re.sub('\s+',' ',text)

	def passwordVlidator(text,minLength = 5,char = True,digit = True,symbol = False,upperCase = False):
		regex = '(?={' + minLength + ',})';
		regex += '(?=.+[a-zA-Z])' if char else ''
		regex += '(?=\d)' if digit else ''
		regex += '(?=\W+)' if symbol else ''
		m = re.findall(regex)
		return m


