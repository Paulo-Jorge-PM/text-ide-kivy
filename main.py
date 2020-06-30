#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.clock import Clock
from kivy.uix.recycleview import RecycleView

from gui.textMain import TextMain
from gui.infoPanel import InfoPanel
from gui.spellcheckPanel import SpellcheckPanel
from gui.morphologyPanel import MorphologyPanel
from gui.sintaxePanel import SintaxePanel
from gui.sentimentPanel import SentimentPanel
from gui.translationPanel import TranslationPanel
from gui.statisticsPanel import StatisticsPanel
from gui.autocomplete import Autocomplete
from gui.dictionaryPanel import DictionaryPanel

from config import config

#import threading
import os

#import multiprocessingste
#from databases import databases
#import sqlite3
#import marisa_trie


### NOTAS:
#The words database was imported from the PT Firefox public dictionary
#Innitialy had the words in csv, later in sqlite, but the autocomeplte code was to slow while typing,
#Tryed to load all the sqlite database in RAM 1st, but still was not fast enough
#So tryed the sqlite part in C, but still was slow,
#After tyed multithreading and multiprocessings, better but not perfect yet.
#So later gave up on sqlite and adapted it to Patrician Tries (Radix Tree), using a C library, and worked like a charm
#To do: add multithreading to Patrician Trie so it goes even faster?

#TO DO
#quando palavra não existe dá um Error in sys.excepthook na consola. não interfere nem crasha, mas convém limpar isso

#Backup das versões e experiências em sqlite, C, e multithreadings
"""import ctypes
from ctypes import *

adder = CDLL('./c/adder.so')"""

#db = databases.Databases()

#pragmas = [ ('journal_mode', 'wal'), ('cache_size', -1000 * 32)]

### TO DO FIXED CONFIGURATIONS IN AN EXTERNAL FILE ###
#language = 'pt-pt'

#sqlite 1st version, moved to external file. delete if patrician tries work better
"""
class databases():

    db_path = os.path.join('databases', language)
    db_words_path = os.path.join(db_path, 'words.sqlite')

    self.db = sqlite_connection(db_words_path)
    self.cursor = db.cursor()

    def sqlite_connection(self, path):
        return sqlite3.connect(path, check_same_thread=False)

    def words_query(self):"""
#        return self.cursor.execute('SELECT word FROM words WHERE id > 0')

#    def synonyms_query(self, word):
#        return self.cursor.execute('SELECT synonym FROM words WHERE word = ?', (word,))

#    def antonyms_query(self):
#        pass


"""class trie(db_cursor):

    self.trie = marisa_trie.Trie(self.make_list(db_cursor))

    def make_list(self, cursor):
        words_list = []
        for word in cursor:
            words_list.append(word[0])
        return words_list

    def trie_query(word):"""
#        data = [{'value': x} for x in self.trie.keys(word)]
#        return data




#db_path = os.path.join('databases', language)
#db_words = os.path.join(db_path, 'words_fts5.sqlite')
#db_words = os.path.join(db_path, 'words.sqlite')
#db_main = sqlite3.connect(db_words, check_same_thread=False)

#def db_query(word, db):
#    cursor = db_main.cursor()
    #cursor.execute('SELECT word FROM words WHERE word LIKE ? limit 5', (word+'%',))
    #cursor.execute('SELECT word FROM words WHERE id>5 AND id <200')
    #cursor.execute('SELECT word FROM words WHERE INSTR(word, "paul") > 0')
#    cursor.execute('SELECT word FROM words WHERE word MATCH ?', (word+'*',))
#    data = [{'value': x[0]} for x in cursor]
    #print(data)
    #data = []
#    return data




#Prefix Tree using marisa_trie python binding from c
#trie = marisa_trie.Trie([u'key1', u'key2', u'key12'])

"""
words_list = []
cursor = db_main.cursor()"""
#cursor.execute('SELECT word FROM words WHERE id>0')
"""for word in cursor:
    words_list.append(word[0])
print("TRIE done")
trie = marisa_trie.Trie(words_list)

def trie_query(word):
"""
    #data = [{'value': x} for x in trie.keys(word)]
    #return data


#convert from sqlite file in disk to a temporary db in memory, for faster queries
"""def sqlite_file_to_memory(db_file):
    import io

    # Read database to tempfile
    con = sqlite3.connect(db_file)
    tempfile = io.StringIO()
    for line in con.iterdump():
        tempfile.write('%s\n' % line)
    con.close()
    tempfile.seek(0)

    # Create a database in memory and import from tempfile
    db_memory = sqlite3.connect(":memory:")
    db_memory.cursor().executescript(tempfile.read())
    db_memory.commit()
    db_memory.row_factory = sqlite3.Row
    return db_memory"""


#memory version teste
#db_main = sqlite_file_to_memory(db_words)



class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Load configs for global access on the GUI
        self.config = config

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.text_main.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        text = self.ids.text_main.text
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(text)

        self.dismiss_popup()

    #def word_count(self):
    #    self.ids.word_list.text = 'ttt'



class RecycleViewRow(BoxLayout):
    value = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()


class Editor(App):

    #so other widgets can acess it easily
    def build(self):
        #global root
        #root = self.root
        #return TextMain()
        pass

    #def text_change(self, text):
    #    self.root.ids.word_list.text = text

    def word_count(self):
        print('word_count')
        #self.root.ids.word_list.text = 'ttt'


### GUI
#TextMain = TextMain()
#InfoPanel = InfoPanel()ee  ano

#O Factory regista classes para que possam ser usadas diretamente no kv. Útil para fazer um sub-class e manipular aqui 1º antes de definir no kv
Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

Factory.register('TextMain', cls=TextMain)
Factory.register('InfoPanel', cls=InfoPanel)
Factory.register('SpellcheckPanel', cls=SpellcheckPanel)
Factory.register('MorphologyPanel', cls=MorphologyPanel)
Factory.register('SintaxePanel', cls=SintaxePanel)
Factory.register('SentimentPanel', cls=SentimentPanel)
Factory.register('TranslationPanel', cls=TranslationPanel)
Factory.register('StatisticsPanel', cls=StatisticsPanel)
Factory.register('Autocomplete', cls=Autocomplete)
Factory.register('DictionaryPanel', cls=DictionaryPanel)

if __name__ == '__main__':
    #Go fullscreen
    #from kivy.core.window import Window
    #Window.fullscreen = 'auto'
    #Config.set('graphics', 'window_state', 'maximized')
    #Config.write()
    Config.read('config_kivy.ini')
    Config.write()
    #db = Databases()
    Editor().run()
