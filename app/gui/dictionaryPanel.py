#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.rst import RstDocument

from core.dictionary import Dictionary

import re

class DictionaryPanel(RstDocument):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

    def build(self):
        pass

    def check(self, word, lang):
        dictionary = Dictionary(word, lang=lang)
        definitions = dictionary.definition()
        examples = dictionary.example()

        self.info(word, lang, definitions, examples)

    def info(self, word, lang, definitions, examples):

        info = '''

:CURRENT WORD:
    ''' + word + '''
    
:LANGUAGE:
    ''' + lang + '''

----

:DEFINITION:'''

        for d in definitions:
            info += '''
    ["''' + d + '''"]
'''

        info += '''

----

:USE CASES:'''

        for e in examples:
            if e:
                info += '''
    ''' + repr(e) + '''
'''

        self.text = info

#if __name__ == '__main__':
#    main = InfoPanel()
