#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from spellchecker import SpellChecker

class Spellcheck:

    def __init__(self, words=[], lang='pt-pt'):
        if lang=='pt-pt' or lang=='por':
            self.lang = 'pt'
        else:
            self.lang = 'en'

        self.spell = self.check(words)

    def check(self, words=[]):
        spell = SpellChecker(language=self.lang)
        misspelled = words
        misspelled = spell.unknown(misspelled)
        corrected = []
        for word in words:
            result = {}
            if word.lower() in misspelled:
                result["original"] = word
                result["corrected"] = spell.correction(word)
                result["candidates"] = spell.candidates(word)
            else:
                result["original"] = word
                result["corrected"] = word
                result["candidates"] = ''
            corrected.append(result)
        return corrected

if __name__ == '__main__':
    main = Spellcheck(['dogg', 'animal'], lang='en')
    print(main.spell)
