#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.rst import RstDocument

from core.spellcheck import Spellcheck

import re
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

class SpellcheckPanel(RstDocument):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

    def build(self):
        pass

    def check(self, text='', lang='pt-pt'):
        words = nltk.word_tokenize(text)
        spellcheck = Spellcheck(words, lang=lang).spell
        #self.checkWord(tokens)
        self.show(spellcheck, text)


        #if word != '':
        #    spell = self.checkWord(word)
        #    print(spell)
        #if text != '':
        #    pass

    # def checkWord(self, words):
    #     spellcheck = Spellcheck(words)
    #     exist = 'Word not found'
    #     for w in spellcheck.spell:
    #         if w[0] == word:
    #             exist = 'Word found'
    #     return dict(exist=exist, alternatives=spellcheck.spell)

    def untokanize(self, tokes):
        text = TreebankWordDetokenizer().detokenize(tokens)
        return text

    def show(self, words, txt):
        
        original = txt
        checked = ''
        alternatives = ''

        for w in words:
            if w['original'] == w['corrected']:
                checked += w['original'] + ' '
                #checked += '\[color\=#00FF00\]' + w['original'] + '\[\/color\]'
            else:
                red = '\[color\=#ff0000\]' + w['original'] + '\[\/color\]'
                original = original.replace(w['original'], red)
                checked += '\[b\]' + w['corrected'] + '\[\/b\] '
                alternatives += w['original'] + ': ' + ' / '.join(w['candidates'])[2:] + '''\n
    '''

        info = '''

:CURRENT PHRASE:
    {}
    
:SPELCHECKED:
    {}

:ALTERNATIVES:
    {}

        '''.format(original, checked, alternatives)
        
        self.text = info

#if __name__ == '__main__':
#    main = InfoPanel()
