# coding: utf8
"""
Complete collection of Urdu alphabet.
"""
from __future__ import unicode_literals

# Common Urdu alphabet
URDU_ALPHABET = set("""

  آ أ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ
 س ش ص ض ط ظ ع غ ف ق ك ک گ ل م ن ں و ؤ ہ ه ھ ء ی ے ‬

 ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹

""".split())

# Complete set of Urdu alphabet. Unicode Range (0600 - 06ff)
# http://jrgraphix.net/r/Unicode/0600-06FF
# https://www.unicode.org/charts/PDF/U0600.pdf
URDU_ALPHABET_COMPLETE = set("""

 ؀ ؁ ؂ ؃ ؄ ؅ ؆ ؇ ؈ ؉ ؊ ؋ ، ؍ ؎ ؏ ؐ ؑ ؒ ؓ ؔ ؕ ؖ ؗ ؘ ؙ ؚ ؛ ؜ ؝ ؞ ؟
 ؠ ء آ أ ؤ إ ئ ا ب ة ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ػ ؼ ؽ ؾ ؿ
 ـ ف ق ك ل م ن ه و ى ي ً ٌ ٍ َ ُ ِ ّ ْ ٓ ٔ ٕ ٖ ٗ ٘ ٙ ٚ ٛ ٜ ٝ ٞ ٟ
 ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ ٪ ٫ ٬ ٭ ٮ ٯ ٰ ٱ ٲ ٳ ٴ ٵ ٶ ٷ ٸ ٹ ٺ ٻ ټ ٽ پ ٿ
 ڀ ځ ڂ ڃ ڄ څ چ ڇ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ڑ ڒ ړ ڔ ڕ ږ ڗ ژ ڙ ښ ڛ ڜ ڝ ڞ ڟ
 ڠ ڡ ڢ ڣ ڤ ڥ ڦ ڧ ڨ ک ڪ ګ ڬ ڭ ڮ گ ڰ ڱ ڲ ڳ ڴ ڵ ڶ ڷ ڸ ڹ ں ڻ ڼ ڽ ھ ڿ
 ۀ ہ ۂ ۃ ۄ ۅ ۆ ۇ ۈ ۉ ۊ ۋ ی ۍ ێ ۏ ې ۑ ے ۓ ۔ ە ۖ ۗ ۘ ۙ ۚ ۛ ۜ ۝ ۞ ۟
 ۠ ۡ ۢ ۣ ۤ ۥ ۦ ۧ ۨ ۩ ۪ ۫ ۬ ۭ ۮ ۯ ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ ۺ ۻ ۼ ۽ ۾ ۿ

""".split())

# Urdu punctuation
URDU_PUNCTUATION = set("""

 ؛ ، ٠  ٫ ـ ؟ ۔ ٭ ٬ ٪

""".split())
