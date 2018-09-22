# coding=utf-8
""""Generate Unicode mapping for Urdu character"""

from pyuca import Collator

c = Collator()

###########################################################################
# Digits from 0 to 9
URDU_DIGITS = frozenset(""" ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ """.replace(" ", ""))
URDU_DIGITS_UNICODE_MAPPING_INTEGER = {}
URDU_DIGITS_UNICODE_MAPPING_HEX = {}
for c in sorted(URDU_DIGITS, key=c.sort_key):
    URDU_DIGITS_UNICODE_MAPPING_INTEGER[c] = ord(c)
    URDU_DIGITS_UNICODE_MAPPING_HEX[c] = '%04x' % ord(c)

print(URDU_DIGITS_UNICODE_MAPPING_INTEGER)
print(URDU_DIGITS_UNICODE_MAPPING_HEX)

###########################################################################
# Complete set of Urdu alphabet
URDU_ALPHABET_COMPLETE = frozenset("""

  آ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ
 س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ؤ ہ ه ھ ء ی ئ ے ‬

""".replace(" ", "").replace("\n", ""))

URDU_ALPHABET_COMPLETE_UNICODE_MAPPING_INTEGER = {}
URDU_ALPHABET_COMPLETE_UNICODE_MAPPING_HEX = {}
for c in sorted(URDU_ALPHABET_COMPLETE, key=c.sort_key):
    URDU_ALPHABET_COMPLETE_UNICODE_MAPPING_INTEGER[c] = ord(c)
    URDU_ALPHABET_COMPLETE_UNICODE_MAPPING_HEX[c] = '%04x' % ord(c)

print(URDU_ALPHABET_COMPLETE_UNICODE_MAPPING_INTEGER)
print(URDU_ALPHABET_COMPLETE_UNICODE_MAPPING_HEX)
