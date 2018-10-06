# coding: utf8
""" Test cases """

from urdu_alphabet import URDU_ALPHABET, URDU_DIGITS, URDU_PUNCTUATION, DIACRITICS
import re

urdu_unicode_range = re.compile("[^\u0600-\u06ff \u202c\n]+")


class TestUrduAlphabet(object):
    """Test cases for Urdu Alphabet"""

    def test_urdu_alphabet(self):
        """ Test urdu_alphabet"""
        assert len(URDU_ALPHABET) == 44
        for character in URDU_ALPHABET:
            assert len(urdu_unicode_range.findall(character)) == 0

    def test_urdu_digits(self):
        """ Test """
        assert len(URDU_DIGITS) == 11
        for character in URDU_DIGITS:
            assert len(urdu_unicode_range.findall(character)) == 0

    def test_urdu_punctuation(self):
        """ Test """
        assert len(URDU_PUNCTUATION) == 7
        for character in URDU_PUNCTUATION:
            assert len(urdu_unicode_range.findall(character)) == 0

    def test_diacritics(self):
        """ Test """
        assert len(DIACRITICS) == 6
        for character in DIACRITICS:
            assert len(urdu_unicode_range.findall(character)) == 0
