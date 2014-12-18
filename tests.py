import unittest
from common_regex import CommonRegex
class TestRegexUtil(unittest.TestCase):

    def setUp(self):
        self.dummy_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self.strong_password = "Word$Numb3rs"
        self.weak_password = "weak"

    def test_find_words(self):
        words   = RegexUtil.find_words(self.dummy_text)
        words_10= RegexUtil.find_words(self.dummy_text, 10)

        self.assertEqual(len(words),69)
        self.assertTrue(len(words) >= len(words_10))
        for word in words_10:
            self.assertTrue(len(word) >= 10)

    def test_find_links(self):
        pass

    def test_match_arabic(self):
        pass

    def test_password_vlidator(self):
        self.assertTrue(RegexUtil.password_validator(self.strong_password, min_length=10, char=True, digit=True, symbol=True, upper_case=True))
        self.assertFalse

if __name__ == '__main__':
    unittest.main()