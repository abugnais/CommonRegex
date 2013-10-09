import re
class RegexUtil:
	@staticmethod
	def findWords(text,minLength=1):
		m = re.search('\w{' + minLength + ',}',text)
		return m

	def findLinks(text):
		m = re.search('\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))',text)
		return m

	def matchArabic(text):
		m = re.search('([\x{0621}-\x{0670}]+)',text)
		return m

	def findControlChars(text):
		m = re.search('(?![\x{000d}\x{000a}\x{0009}])\p{C}')
		return m

	def twitterNames(text):
		m = re.search('@\w{1,15}')
		return m

	def hashtags(text):
		m = re.search('#\w+')
		return m

	def findEmails(text):
		m = re.search('[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?',text)
		return m

	def findNumbers(text):
		m = re.search('\d+',text)
		return m

	def removeExtraSpaces(text):
		return re.sub('\s+',' ',text)

	def passwordVlidator(text,minLength = 5,char = true,digit = true,symbol = false,upperCase = false):
		regex = '(?={' + minLength + ',})';
		regex += char ? '(?=.+[a-zA-Z])' : ''
		regex += digit ? '(?=\d)' : ''
		regex += symbol ? '(?=\W+)' : ''
		m = re.search(regex)
		return m


