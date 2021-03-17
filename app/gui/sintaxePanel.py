#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.rst import RstDocument
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
import kivy.uix.button as btn
from kivy.uix.label import Label

from kivy.app import App
from kivy.uix.widget import Widget

import re
import nltk
import threading

from core.sintaxe import Sintaxe


class SintaxePanel(FloatLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

        buttonSintaxe = btn.Button(text='Draw tree', pos_hint= {'x': 0.01,'top': 0.95},size_hint = (.1,.1))
        self.add_widget(buttonSintaxe)
        buttonSintaxe.bind(on_press=self.draw)

        self.rst = RstDocument()
        self.rst.pos_hint= {'x': 0,'top': 0.8}
        self.rst.background_color = (0.5, 1, 0.5, 0)
        self.rst.scroll_type = ['bars']
        #self.rst.bar_width = dp(10)
        self.rst.bar_color = [0.658, 0.658, 0.658, 1]
        self.rst.bar_inactive_color = [0.756, 0.756, 0.756, 1]
        self.add_widget(self.rst)

        self.sintaxe = None


    def build(self):
        pass

    def check(self, text, lang):
        self.getTree(text,lang)
        self.rst.text = '''

:CURRENT PHRASE:
    {}
    
:SINTAXE PARSED:
    {}

'''.format(text, repr(self.sintaxe.tree))

    def getTree(self, text, lang):
        if not self.sintaxe:
            self.sintaxe = Sintaxe(lang=lang)
        self.sintaxe.generate(text)

    def draw(self, value):
        self.sintaxe.draw(self.sintaxe.tree)


#if __name__ == '__main__':
#    main = InfoPanel()
