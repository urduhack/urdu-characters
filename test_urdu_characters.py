# coding: utf8
""" Test cases """
import re
import unicodedata

from urdu_characters import (URDU_ALL_CHARACTERS, URDU_ALPHABETS, URDU_DIGITS, URDU_PUNCTUATIONS, URDU_DIACRITICS,
    URDU_ALL_CHARACTERS_UNICODE, )

URDU_UNICODE_RANGE = re.compile("[^\u0600-\u06ff]+")


class TestUrduAlphabet():
    """Test cases for Urdu Alphabet"""

    def test_urdu_alphabet(self):
        """ Test urdu_alphabet"""
        for character in URDU_ALPHABETS:
            assert character in URDU_ALL_CHARACTERS
            assert len(character) == 1
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0

    def test_urdu_digits(self):
        """ Test """
        for character in URDU_DIGITS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0

    def test_urdu_punctuation(self):
        """ Test """
        for character in URDU_PUNCTUATIONS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0

    def test_diacritics(self):
        """ Test """
        for character in URDU_DIACRITICS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0

    def test_unicode(self):
        """ Test """
        for character in URDU_ALL_CHARACTERS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS_UNICODE

        for character, value in URDU_ALL_CHARACTERS_UNICODE.items():
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS
            assert value in URDU_ALL_CHARACTERS

        tmp = set()
        for character, value in URDU_ALL_CHARACTERS_UNICODE.items():
            tmp.add(value)

        for character in URDU_ALL_CHARACTERS:
            assert len(character) == 1
            assert character in tmp

    def test_unicode_norm(self):
        """Test case"""
        for character in URDU_ALL_CHARACTERS:
            if character == "ئ":
                continue
            characters = unicodedata.normalize('NFKD', character)
            for char in characters:
                assert char in URDU_ALL_CHARACTERS, characters

    def test_check_data(self):
        """Data Type Check of all the elements"""
        assert isinstance(URDU_ALPHABETS, frozenset)
        assert isinstance(URDU_ALL_CHARACTERS, frozenset)
        assert isinstance(URDU_UNICODE_RANGE, frozenset)
        assert isinstance(URDU_ALL_CHARACTERS_UNICODE, frozenset)
        assert isinstance(URDU_DIACRITICS, frozenset)
        assert isinstance(URDU_DIGITS, frozenset)
        assert isinstance(URDU_PUNCTUATIONS, frozenset)
