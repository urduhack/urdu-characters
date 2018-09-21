# coding: utf8
"""
Complete collection of Urdu alphabet.
"""
from __future__ import unicode_literals


# Digits from 0 to 9
URDU_DIGITS = frozenset(""" ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ """)


# Complete set of Urdu alphabet
URDU_ALPHABET_COMPLETE = frozenset("""

  آ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ
 س ش ص ض ط ظ ع غ ف ق ك ک گ ل م ن ں و ؤ ہ ه ھ ء ی ے ‬

""".split())


# Urdu punctuation
URDU_PUNCTUATION = frozenset("""

 ؛ ، ٠  ٫ ـ ؟ ۔ ٭ ٬ ٪

""".split())
