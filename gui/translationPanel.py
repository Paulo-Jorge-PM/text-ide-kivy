#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.rst import RstDocument

from core.translation import Translation

class TranslationPanel(RstDocument):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

        self.translation = None

    def build(self):
        pass

    def check(self, text='', lang='pt-pt'):
        if not self.translation:
            self.translation = Translation(lang=lang)
        translated = self.translation.translate(text)
        
        if lang =='pt-pt':
            origin_lang = 'Portuguese'
            target_lang = 'English'
        else:
            origin_lang = 'English'
            target_lang = 'Portuguese'
            
        self.show(translated, text, origin_lang, target_lang)

    def show(self, translated, txt, origin_lang, target_lang):

        info = '''

:CURRENT PHRASE:
    {}

:ORIGIN LANG:
    {}

:TRAGET LANG:
    {}

:TRANSLATED:
    {}

'''.format(txt, origin_lang, target_lang, translated)
        
        self.text = info

#if __name__ == '__main__':
#    main = InfoPanel()
