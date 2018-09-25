# coding: utf8
"""Complete collection of Urdu alphabet."""
from __future__ import unicode_literals

# Complete set of Urdu alphabet.
URDU_ALPHABET_COMPLETE = frozenset("""

  آ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ
 س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ؤ ہ ه ھ ء ی ئ ے ‬

""".split())

# Urdu Digits from 0 to 9
URDU_DIGITS = frozenset(""" ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ """)

# Urdu punctuation
URDU_PUNCTUATION = frozenset("""

 ؛ ، ٫ ـ ؟ ۔ ٪

""".split())

ARABIC_SYMBOLS = frozenset(""" ﷺ """)

ALL_CHARACTERS = URDU_ALPHABET_COMPLETE | URDU_DIGITS | URDU_PUNCTUATION | ARABIC_SYMBOLS
