#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.recycleview import RecycleView

import os.path
import threading

from core import databases
from core import tries
from config import config
#import multiprocessing
#from databases import databases

#import sqlite3
#import marisa_trie

#=== IMPORTANT VARS ===#
#WORD = ''
#PARAGRAPH = ''


db_path = os.path.join('databases', config.language)
db_words_path = os.path.join(db_path, 'words.sqlite')

db = databases.Database(db_words_path)
trie = tries.Trie(db.words())

"""import ctypes
from ctypes import *

adder = CDLL('./adder.so')"""

#TO DO
#quando palavra não existe dá um Error in sys.excepthook na consola. não interfere nem crasha, mas convém limpar isso



#db = databases.Databases()

#pragmas = [ ('journal_mode', 'wal'), ('cache_size', -1000 * 32)]

### FIXED CONFIGURATIONS FOR AN EXTERNAL FILE ###
#language = 'pt-pt'

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
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    #def word_count(self):
    #    self.ids.word_list.text = 'ttt'



class TextMain(TextInput):

    word = StringProperty('')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

    #global root
    #root.ids.word_list.text = 'ppppp'

    def build(self):
        self.bind(text=on_text)

    def on_text(self, instance, value):
        #app = App.get_running_app()
        #WORD = self.select_word()
        self.word = self.select_word()
        #app.root.ids.word_list.text = WORD

        #[{'value':'novo'}]
        #app.root.ids.list_synonyms.make_data(WORD)


        #app.root.ids.list_words.data = Clock.schedule_once( self.get_words(WORD), -1)
        #app.root.ids.middle_bottom_content.text = WORD + " (" + str(len(WORD)) + ")"

        #run list updates
        #ListWords().make_data()
        #ListWords().refresh()
    #def test(self, value,db):
    #        return db_query(value,db)

    def on_word(self, instance, value):
        #self.app.root.ids.list_words.data = self.get_words(value)

        tab = self.app.root.ids.tabs_left.current_tab.text

        if tab == "Words":
            self.get_words(value)
        elif tab == "Synonyms":
            self.get_synonyms(value)

        #thread = threading.Thread(target=self.get_words, args=(value,))
        #thread.start()
        #process = multiprocessing.Process(target=self.get_words, args=(value,))
        #process.start()

        #pool = multiprocessing.Pool(processes=4)
        #process = pool.apply_async(self.test, args=(value,db_main))

        #output = process.get()
        #print(output)




        #App.get_running_app().root.ids.middle_bottom_content.text = value + " (" + str(len(value)) + ")"
        #App.get_running_app().root.ids.middle_bottom_content.text = value + " (" + str(len(value)) + ")"
        #adder.words("pau")


        ####== C DB VERSION ==###
        """c_func = adder.words
        c_func.restype = c_char_p
        result = c_func("paul")"""

        #c_func.argtypes = [c_char_p]
        #w = create_string_buffer("paul")
        #w = create_string_buffer(b"paul")
        #c_func(repr(w.raw))
        #ctypes.pointer(c_f)
        #print ( result )

    def get_words(self, word):
        #data = [{'value': x} for x in list(word)]
        #db_temp = ['paulo', 'pauta', 'pausa', 'poeta', 'poente', 'praia', 'palácio', 'piscina', 'pincel', 'prado', 'pardo', 'prego', 'premiar', 'pacto', 'prémio', 'pantano', 'puro', 'para', 'parar', 'pálido']
        """if len(word) > 9:
            words = db.get_words(word)
            #data = [{'value': x} for x in words if x.startswith(word) and word]
            data = [{'value': x} for x in words]
            return data
        else:
            data = []
            return data"""

        #data = [{'value': x} for x in words if x.startswith(word) and word]
        #for w in words:
        #    print('a')
        if len(word) > 1:
            #print(11111111)
            #words = db.get_words(word)
            #data = [{'value': x[0]} for x in words]
            #data = Clock.schedule_once( db.get_words(word), -1 )
            """words = db.get_words(word)
            print(2222222222)
            data = [{'value': x[0]} for x in words]"""
            #data = db_query(word, db_main)
            data = trie.trie_query(word.lower())
        else:
            data = []
        #print(data)
        self.app.root.ids.list_words.data = data
        #print(WORD)
        #return data

    #code from on_double_tap()
    def select_word(self):
        ci = self.cursor_index()
        cc = self.cursor_col
        line = self._lines[self.cursor_row]
        len_line = len(line)
        #start = max(0, len(line[:cc]) - line[:cc].rfind(u' ') - 1)
        start = max(0, len(line[:cc]) - line[:cc].rfind(u' '))
        #start = start if start[0] != " " else (start-1)
        end = line[cc:].find(u' ')
        end = end if end > - 1 else (len_line - cc)
        #Save de default selection_color before hiding it with alpha 0
        selection_color = self.selection_color
        self.selection_color=[0,0,0,0]
        self.select_text(ci - start, ci + end)
        word = self.selection_text.strip()
        #transform all input to .lower() ? or do it in db selection, not case sensitive?
        self.cancel_selection()
        #Restore default selection_color
        self.selection_color = selection_color
        return(word)

    def get_antonyms(self, word):
        pass

    def get_synonyms(self, word):
        if len(word) > 1:
            data = [{'value': x} for x in db.synonyms(word)]
            self.app.root.ids.list_synonyms.data = data

class RecycleViewRow(BoxLayout):
    #text = StringProperty()
    value = StringProperty()

class ListWords(RecycleView):

    def __init__(self, *args, **kwargs):
        super(ListWords, self).__init__(*args, **kwargs)

        #self.data = [{'text': "Button " + str(x), 'id': str(x)} for x in range(3)]
        #self.data = [{'text':'111111', 'id':'synonym_list1'}, {'text':'222222','id':'synonym_list2'}]

        #lista = list(WORD)
        #self.data = [{'value':'Palavra 1'}, {'value':'Palavra 2'}]
        #self.data = [{'value': x} for x in list(WORD)]

        #self.word = WORD.get()
        #self.data = [{'value': x} for x in list(self.word)]
        #self.make_data(WORD)
        self.make_data('teste')


        #self.word = word
        #self.type = type


    def words(self):
        pass

    def synonyms(self):
        pass

    def clear(self):
        self.data = []

    def make_data(self, word):
        self.data = [{'value': x} for x in list(word)]

    def refresh(self):
        if self.data:
            self.refresh_from_data()

    def list(self):
        pass

    def gui(self):
        pass

#class Synonyms():
#    pass

#class Antonyms():
#    pass



    #def on_text(self, instance, value):
    #    print('The widget', instance, 'have:', value)

    #def __init__(self, **kwargs):
    #    super(TextMain, self).__init__(**kwargs)
    #pass
    #def __init__(self):

     #   self.ids.word_list.text = 'ttt'

     #   self.insert_text(s, from_undo=from_undo)
    #def insert_text(self, substring, from_undo=False):
        #s = substring.upper()
        #return super(TextMain, self).insert_text(s, from_undo=from_undo)

    #def on_text(self, instance, value):
    #    print('The widget', instance, 'have:', value)

    #def build(self):
        #return TextInput(text='Hello world')


#class WordCount():

#    def word_count(self):
#        self.ids.word_list.text = 'ttt'


#class TabsLeft(TabbedPanel):
#    pass



class Editor(App):
    #so other widgets can acess it easily
    def build(self):
        #global root
        #root = self.root
        #return TextMain()
        pass

    #db = Databases()


    #def build(self):
        #return TextMain()

    #def text_change(self, text):
    #    self.root.ids.word_list.text = text

    """
    def on_double_tap(self):
        ci = self.cursor_index()
        cc = self.cursor_col
        line = self._lines[self.cursor_row]
        len_line = len(line)
        start = max(0, len(line[:cc]) - line[:cc].rfind(u' ') - 1)
        end = line[cc:].find(u' ')
        end = end if end > - 1 else (len_line - cc)
        Clock.schedule_once(lambda dt: self.select_text(ci - start, ci + end))
    """

    def word_count(self):
        pass
        #self.root.ids.word_list.text = 'ttt'


#O Factory regista classes para que possam ser usadas diretamente no kv. Útil para fazer um sub-class e manipular aqui 1º antes de definir no kv
Factory.register('Root', cls=Root)
Factory.register('TextMain', cls=TextMain)
Factory.register('ListWords', cls=ListWords)

Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)



if __name__ == '__main__':
    #Go fullscreen
    #from kivy.core.window import Window
    #Window.fullscreen = 'auto'
    #Config.set('graphics', 'window_state', 'maximized')
    #Config.write()
    Config.read('config.ini')
    Config.write()
    #db = Databases()
    Editor().run()
