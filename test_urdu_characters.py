# coding: utf8
""" Test cases """
import re
import unicodedata

from urdu_characters import (URDU_ALL_CHARACTERS, URDU_ALPHABETS, URDU_DIGITS, URDU_PUNCTUATIONS, URDU_DIACRITICS,
                             URDU_ALL_CHARACTERS_UNICODE, URDU_EXTRA_CHARACTERS)

URDU_UNICODE_RANGE = re.compile("[^\u0600-\u06ff]+")


class TestUrduAlphabet():
    """Test cases for Urdu Alphabet"""

    def test_urdu_alphabet(self):
        """ Test urdu_alphabet"""
        assert 46 == len(URDU_ALPHABETS)
        assert isinstance(URDU_ALPHABETS, frozenset)
        for character in URDU_ALPHABETS:
            assert character in URDU_ALL_CHARACTERS
            assert len(character) == 1
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0
            assert isinstance(character, str)

    def test_urdu_digits(self):
        """ Test """
        assert 10 == len(URDU_DIGITS)
        assert isinstance(URDU_DIGITS, frozenset)
        for character in URDU_DIGITS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0
            assert isinstance(character, str)

    def test_urdu_punctuation(self):
        """ Test """
        assert 6 == len(URDU_PUNCTUATIONS)
        assert isinstance(URDU_PUNCTUATIONS, frozenset)
        for character in URDU_PUNCTUATIONS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0
            assert isinstance(character, str)

    def test_diacritics(self):
        """ Test """
        assert 6 == len(URDU_DIACRITICS)
        assert isinstance(URDU_DIACRITICS, frozenset)
        for character in URDU_DIACRITICS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0
            assert isinstance(character, str)

    def test_extras_characters(self):
        """ Test """
        assert 22 == len(URDU_EXTRA_CHARACTERS)
        assert isinstance(URDU_EXTRA_CHARACTERS, frozenset)
        for character in URDU_EXTRA_CHARACTERS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0
            assert isinstance(character, str)

    def test_unicode(self):
        """ Test """
        for character in URDU_ALL_CHARACTERS:
            assert len(character) == 1
            assert character in URDU_ALL_CHARACTERS_UNICODE
            assert isinstance(character, str)

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
        assert isinstance(URDU_ALL_CHARACTERS, frozenset)
        assert isinstance(URDU_ALL_CHARACTERS_UNICODE, dict)
        assert 90 == len(URDU_ALL_CHARACTERS)
        assert len(URDU_ALL_CHARACTERS_UNICODE) == len(URDU_ALL_CHARACTERS)
