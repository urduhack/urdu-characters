# coding: utf8
""" Test cases """

from urdu_alphabet import URDU_CHARACTERS, URDU_ALPHABET, URDU_DIGITS, URDU_PUNCTUATIONS, URDU_DIACRITICS
import re

urdu_unicode_range = re.compile("[^\u0600-\u06ff]+")


class TestUrduAlphabet(object):
    """Test cases for Urdu Alphabet"""

    def test_urdu_alphabet(self):
        """ Test urdu_alphabet"""
        for character in URDU_ALPHABET:
            assert character in URDU_CHARACTERS
            assert len(urdu_unicode_range.findall(character)) == 0

    def test_urdu_digits(self):
        """ Test """
        for character in URDU_DIGITS:
            assert character in URDU_CHARACTERS
            assert len(urdu_unicode_range.findall(character)) == 0

    def test_urdu_punctuation(self):
        """ Test """
        for character in URDU_PUNCTUATIONS:
            assert character in URDU_CHARACTERS
            assert len(urdu_unicode_range.findall(character)) == 0

    def test_diacritics(self):
        """ Test """
        for character in URDU_DIACRITICS:
            assert character in URDU_CHARACTERS
            assert len(urdu_unicode_range.findall(character)) == 0
