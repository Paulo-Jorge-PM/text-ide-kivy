#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.rst import RstDocument
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from core.statistics import Statistics

class StatisticsPanel(RstDocument):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

    def build(self):
        pass

    def check(self, text='', lang='pt-pt'):
        if text:
            words = Statistics().countWords(text)
            chars = Statistics().countCharacters(text)
            paragraphs = Statistics().countParagraphs(text)
            phrases = Statistics().countPhrases(text)
        else:
            words = chars = paragraphs = phrases = '0'
        self.show(words, chars, paragraphs, phrases)

    def CharactersCount(self, text):
        count = Statistics().countCharacters(text)
        self._popup = Popup(title="No. of Characters", content=Label(text=count),
                    size_hint=(None, None), size=(300, 200))
        self._popup.open()

    def WordCount(self, text):
        count = Statistics().countWords(text)
        self._popup = Popup(title="No. of Words", content=Label(text=count),
                    size_hint=(None, None), size=(300, 200))
                    #size_hint=(0.9, 0.9))
        self._popup.open()

    def PragraphCount(self, text):
        count = Statistics().countParagraphs(text)
        self._popup = Popup(title="No. of Paragraphs", content=Label(text=count),
                    size_hint=(None, None), size=(300, 200))
        self._popup.open()

    def show(self, words, chars, paragraphs, phrases):

        info = '''

:TOTAL WORDS:
    {}

:TOTAL CHARACTERS:
    {}

:TOTAL PARAGRAPHS:
    {}

:TOTAL PHRASES:
    {}

'''.format(words, chars, paragraphs, phrases)
        
        self.text = info

# class WordCount(Popup):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.app = App.get_running_app()

#     def build(self):
#         pass

#if __name__ == '__main__':
#    main = InfoPanel()
