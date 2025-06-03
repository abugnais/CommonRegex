# -*- coding: utf-8 -*-
import unittest
from common_regex import CommonRegex
class TestCommonRegex(unittest.TestCase):
    dummy_text      = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    strong_password = "Word$Numb3rs"
    weak_password   = "weak"
    arabic_text     = "احمد محمد عمر not arabic text $$##"
    tweet           = "Gary Moore - Parisienne Walkways - Live HD: http://youtu.be/vkUpfw4Hf3w  via @YouTube @AbuGnais"

    def test_find_words(self):
        words   = CommonRegex.find_words(self.dummy_text)
        words_10= CommonRegex.find_words(self.dummy_text, 10)

        self.assertEqual(len(words),69)
        self.assertTrue(len(words) >= len(words_10))
        for word in words_10:
            self.assertTrue(len(word) >= 10)

    def test_find_links(self):
        links = CommonRegex.find_links(self.tweet)
        self.assertListEqual(links, ["http://youtu.be/vkUpfw4Hf3w"])

    def test_twitter_names(self):
        names = CommonRegex.twitter_names(self.tweet)
        self.assertListEqual(names, ["@YouTube", "@AbuGnais"])

    def test_match_arabic(self):
        arabic_words = CommonRegex.match_arabic(self.arabic_text)
        self.assertListEqual(arabic_words, ["احمد", "محمد", "عمر"])
        
    def test_password_vlidator(self):
        self.assertTrue(CommonRegex.password_validator(self.strong_password, min_length=10, char=True, digit=True, symbol=True, upper_case=True))
        self.assertFalse(CommonRegex.password_validator(self.weak_password, min_length=10, char=True, digit=True, symbol=True, upper_case=True))

if __name__ == '__main__':
    unittest.main()