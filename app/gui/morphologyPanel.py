#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.rst import RstDocument

import re
import nltk

from core.morphology import Morphology

class MorphologyPanel(RstDocument):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

    def build(self):
        pass

    def check(self, text, lang):
        morphology = Morphology(text, lang=lang)
        self.show(repr(morphology.tags), repr(morphology.tokens), text)

    def show(self, tags, tokens, text):

        info = '''

:CURRENT PHRASE:
    [ {} ]

:TOKENS:
    [ {} ]

:MORPHOLOGY ANALYSIS:
    [ {} ]

        '''.format(text, tokens, tags)
        
        self.text = info

#if __name__ == '__main__':
#    main = InfoPanel()
