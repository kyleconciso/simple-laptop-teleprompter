# This is a code that utilizes fuzzywuzzy to turn phrases into a soundex string and compared using fuzz ratio

import string
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import fuzzy

def phrase_to_soundex(phrase: str):
    soundex = fuzzy.Soundex(4)
    out = ''.join([soundex(i) for i in phrase.translate(str.maketrans('', '', string.punctuation)).split(' ')])
    return out

def compare_soundex(phrase1: str, phrase2: str):
    return fuzz.ratio(phrase_to_soundex(phrase1), phrase_to_soundex(phrase2))

if __name__ == '__main__':
    while True:
        phrase1 = input('Phrase 1: ')
        phrase2 = input('Phrase 2: ')
        print(compare_soundex(phrase1, phrase2))
