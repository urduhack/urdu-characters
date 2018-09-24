# coding=utf-8
""""Generate Unicode mapping for Urdu character"""

from pyuca import Collator

c = Collator()

URDU_ALL_CHARACTERS = {}
# URDU_ALL_CHARACTERS = URDU_ALPHABET_COMPLETE | URDU_DIGITS | URDU_PUNCTUATION

URDU_ALL_CHARACTERS_UNICODE_MAPPING = {}
for c in sorted(URDU_ALL_CHARACTERS, key=c.sort_key):
    URDU_ALL_CHARACTERS_UNICODE_MAPPING[c] = '%04x' % ord(c)

# print(URDU_ALL_CHARACTERS_UNICODE_MAPPING)
