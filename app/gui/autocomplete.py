#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label

from core.sentiment import SentimentAnalysis

class Autocomplete(RecycleDataViewBehavior, Label):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()


    def build(self):
        pass

    def on_touch_down(self, value):
        print(value)





#if __name__ == '__main__':
#    main = InfoPanel()
