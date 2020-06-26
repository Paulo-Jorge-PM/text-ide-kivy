#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.rst import RstDocument

import re

class InfoPanel(RstDocument):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

    def build(self):
        pass

    def info(self, word, phrase, paragraph):
        wordLen = str(len(word))
        phraseLen = str(len(phrase))
        paragraphLen = str(len(paragraph))

        phraseWords = str(len(phrase.strip().split()))
        paragraphWords = str(len(paragraph.strip().split()))
        paragraphPhrases = len(re.findall(r'\.\s\w|\?\s\w|!\s\w', paragraph ))
        paragraphPhrases = '1' if (paragraphPhrases == 0 and paragraph != '') else '0' if paragraph=='' else str(paragraphPhrases+1)

        info = '''

:CURRENT WORD:
    [ {} ]

    *{} characters*
    
:CURRENT PHRASE:
    [ {} ]

    *{} characters* | *{} words* 

:CURRENT PARAGRAPH:
    [ {} ]

    *{} characters* | *{} words* | *{} sentences* 

        '''.format(word, wordLen, phrase, phraseLen, phraseWords, paragraph, paragraphLen, paragraphWords, paragraphPhrases)

        self.text = info

#if __name__ == '__main__':
#    main = InfoPanel()
