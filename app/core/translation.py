#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, re, pathlib

from textblob import TextBlob

#pip install googletrans
#Google Tradutor
#from googletrans import Translator

class Translation:

    def __init__(self, text='', lang='pt-pt', model=False, lexFolder='SentiLex-PT02'):

        if lang=='pt-pt' or lang=='por':
            self.lang = 'pt'
        else:
            self.lang = 'en'

    def translate(self, text):
        ### USing google translator through the TextBlob library, but could use directly (see comment out code)
        sentence = TextBlob(text)
        try:
            if self.lang != 'en':
                translated = sentence.translate(to='en', from_lang='pt')
            else:
                translated = sentence.translate(to='pt', from_lang='en')
        except:
            log='>>Translation failed for: ' + str(sentence)
            translated = 'Error'

        #googleTranslator = Translator()
        #enGoogle = googleTranslator.translate(text, dest='en', src='pt').text  
        #print(en)
        #print(enGoogle)

        return str(translated)

if __name__ == '__main__':
    main = Translation('pt-pt')
    print(main.translate('Testando o funcionamento do tradutor.'))
