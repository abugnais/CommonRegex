import re

'''
python regualr expressions utility library
to use this library your strings need to be encoded in utf-8
'''
class RegexUtil:
	'''
	returns an array of all the english words in a given text
	@param  string  $text           the text that contains the words
	@param  integer $minLength      optional,the minimum length of the words to find
	@return array
	'''
	@staticmethod
	def findWords(text,minLength=1):
		m = re.findall('\w{' + minLength + ',}',text)
		return m

	'''
	returns an array of valid urls found in the given text
	@param  string $text    the text that contains the links
	@return array
	'''
	def findLinks(text):
		m = re.findall('\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))',text)
		return m

	'''
	matches arabic text and returns and array of all arabic words if the flag $returnMatches is set to true
	@param  string  $text the text to be examined
	@param  bool    $returnMatches optional,if set to true returns an array of the found words
	@return bool|array
	'''
	def matchArabic(text):
		m = re.findall('([\u0621-\u0670]+)',text)
		return m

	'''
	matches all the non printable control characters in a given text
	@param  string $text the text to be examined
	@param  bool   $remove if set to true removes all the control characters from the string $text
	@return bool|string
	'''
	def findControlChars(text):
		m = re.findall('(?![\u000d\u000a\u0009])\p{C}')
		return m

	'''
	matches all the valid twitter screen names in a given text
	@param  string $text
	@return array
	'''
	def twitterNames(text):
		m = re.findall('@\w{1,15}')
		return m

	'''
	matches all the valid twitter hashtags in a given text
	@param  string $text
	@return array
	'''
	def hashtags(text):
		m = re.findall('#\w+')
		return m

	'''
	matches all the valid emails in a given text
	@param  string $text
	@return array
	'''
	def findEmails(text):
		m = re.findall('[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?',text)
		return m

	'''
	matches all the integers in a given text
	@param string $text
	@param integer $minLength the minimum number of digits in the numbers to find
	@param integer $maxLength the maximum number of digits in the numbers to find
	@return array
	'''
	def findNumbers(text):
		m = re.findall('\d+',text)
		return m

	'''
	Removes extra spaces from the given text
	@param string $text
	@return string
	'''
	def removeExtraSpaces(text):
		return re.sub('\s+',' ',text)

	'''
	Checks the given password based on the given validation conditions
	@param string $text the password to be checkes
	@param int $minLength the passwords minimum length default = 6
	@param bool $char   password condition:need to have at least one character default = true
	@param bool $digit  passsword condition:need to have at least one digit default = true
	@param bool $symbol password condition:need to have at least one symbol default = false
	@param bool $upperCase password condition:need to have at least one upper case character default = false
	'''
	def passwordVlidator(text,minLength = 5,char = True,digit = True,symbol = False,upperCase = False):
		regex = '(?={' + minLength + ',})';
		regex += '(?=.+[a-zA-Z])' if char else ''
		regex += '(?=\d)' if digit else ''
		regex += '(?=\W+)' if symbol else ''
		m = re.findall(regex)
		return m


