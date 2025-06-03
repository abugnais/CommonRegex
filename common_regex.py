import re

'''
python regualr expressions utility library
to use this library your strings need to be encoded in utf-8
'''
class CommonRegex:
    '''
    returns an array of all the english words in a given text
    @param  string  text           the text that contains the words
    @param  int minLength      optional,the minimum length of the words to find
    @return array
    '''
    @staticmethod
    def find_words(text,minLength=1):
        return re.findall('\w{' + str(minLength) + ',}',text)

    '''
    returns an array of valid urls found in the given text
    @param  string text    the text that contains the links
    @return array
    '''
    @staticmethod
    def find_links(text):
        return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',text)

    '''
    matches arabic text and returns and array of all arabic words if the flag returnMatches is set to true
    @param  string  text the text to be examined
    @return list
    '''
    @staticmethod
    def match_arabic(text):
        return re.findall('([\u0621-\u0670]+)', text)

    '''
    matches all the non printable control characters in a given text
    @param  string text the text to be examined
    @param  bool   remove if set to true removes all the control characters from the string text
    @return bool|string
    '''
    @staticmethod
    def find_control_characters(text):
        return re.findall('(?![\u000d\u000a\u0009])\p{C}')

    '''
    matches all the valid twitter screen names in a given text
    @param  string text
    @return array
    '''
    @staticmethod
    def twitter_names(text):
        return re.findall('@\w{1,15}', text)

    '''
    matches all the valid twitter hashtags in a given text
    @param  string $text
    @return array
    '''
    @staticmethod
    def hashtags(text):
        return re.findall('#\w+')

    '''
    matches all the valid emails in a given text
    @param  string text
    @return array
    '''
    @staticmethod
    def find_emails(text):
        return re.findall('[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?',text)

    '''
    Returns all of the integer values found in the given text.

    :param str text: Text that may contain integers.
    :return: List of all digit sequences found in ``text``.
    :rtype: list
    '''
    @staticmethod
    def find_numbers(text):
        return re.findall('\d+',text)

    '''
    Removes extra spaces from the given text
    @param string text
    @return string
    '''
    @staticmethod
    def remove_extra_spaces(text):
        return re.sub('\s+',' ',text)

    '''
    Checks the given password based on the given validation conditions
    @param string text the password to be checkes
    @param int min_length the passwords minimum length default = 6
    @param bool char   password condition:need to have at least one character default = true
    @param bool digit  passsword condition:need to have at least one digit default = true
    @param bool symbol password condition:need to have at least one symbol default = false
    @param bool upper_case password condition:need to have at least one upper case character default = false
    '''
    @staticmethod
    def password_validator(text, min_length = 5, char = True, digit = True, symbol = False, upper_case = False):
        regex = '(?=.{' + str(min_length) + ',})';
        regex += '(?=.+[a-zA-Z])' if char else ''
        regex += '(?=.*\d+.*)' if digit else ''
        regex += '(?=.*\W+.*)' if symbol else ''
        return re.compile(regex).match(text) is not None


