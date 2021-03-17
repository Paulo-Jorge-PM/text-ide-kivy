#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.rst import RstDocument

from core.sentiment import SentimentAnalysis

class SentimentPanel(RstDocument):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

        self.sentiment = None

    def build(self):
        pass

    def check(self, text='', lang='pt-pt'):
        if not self.sentiment:
            self.sentiment = SentimentAnalysis(lang=lang)
        polarity = self.sentiment.sentiment(text)
        self.show(polarity, text)

    def show(self, polarity, txt):

        info = '''

:CURRENT PHRASE:
    {}
    
:SENTIMENT:
    {}

        '''.format(txt, polarity)
        
        self.text = info

#if __name__ == '__main__':
#    main = InfoPanel()
