#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

from databases import databases
from databases import tries
from core.dictionary import Dictionary

from config import config

import re, os
import threading
#import multiprocessing

lang = config.lang
db_path = os.path.join('databases', lang)
db_words_path = os.path.join(db_path, 'words.sqlite')

db = databases.Database(db_words_path)
trie = tries.Trie(db.words())

class TextMain(TextInput):

    word = StringProperty('')
    phrase = StringProperty('')
    paragraph = StringProperty('')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()

        #Load configs
        self.lang = config.lang
        self.font_size = config.font_size
        self.font_name = config.font_family
        self.suggest_autocomplete = config.suggest_autocomplete
        self.search_after_n_chars = int(config.search_after_n_chars)
        self.current_cursor = 0

    #global root
    #root.ids.word_list.text = 'ppppp'

    def build(self):
        #self.bind(text=on_cursor)
        #funções on_xxx automaticamente levam bind em alterações no elemento xxx da api
        pass

    def on_text(self, instance, value):
        #panel = self.app.root.ids.tabs_info_panel.current_tab.id
        #switch_to
        if config.fixed_info_panel == 'true':
            self.app.root.ids.tabs_info_panel.switch_to(self.app.root.ids.info)

    def on_cursor(self, instance, value):
        #app = App.get_running_app()
        #WORD = self.select_word()

        #UPDATE DATA
        self.word = self.select_word()
        self.phrase = self.select_phrase()
        self.paragraph = self.select_paragraph()

        #SEND DATA TO THE INFO PANEL
        self.app.root.ids.info_panel.info(self.word, self.phrase, self.paragraph)

        #app.root.ids.word_list.text = WORD

        #[{'value':'novo'}]
        #app.root.ids.list_synonyms.make_data(WORD)


        #app.root.ids.list_words.data = Clock.schedule_once( self.get_words(WORD), -1)
        

        #run list updates
        #ListWords().make_data()
        #ListWords().refresh()
    #def test(self, value,db):
    #        return db_query(value,db)

    def on_word(self, instance, value):
        #self.app.root.ids.list_words.data = self.get_words(value)

        tab = self.app.root.ids.tabs_left.current_tab.text

        if tab == "Words":
            #self.get_words(value)
            thread = threading.Thread(target=self.get_words, args=(value,))
            thread.start()
        elif tab == "Synonyms":
            #self.get_synonyms(value)
            thread = threading.Thread(target=self.get_synonyms, args=(value,))
            thread.start()
        elif tab == "Antonyms":
            #self.get_antonyms(value)
            thread = threading.Thread(target=self.get_antonyms, args=(value,))
            #thread = multiprocessing.Process(target=self.get_antonyms, args=(value,))
            thread.start()

        #panel = self.app.root.ids.tabs_info_panel.current_tab.id

        #if panel == "info":
        #    pass
        #elif panel == "spellcheck":
        #    self.app.root.ids.spellcheck_panel.check(self.phrase)

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

        #Dont want to autocomplete one letter to words, only ater 2 letters:
        if len(word) >= self.search_after_n_chars:
            #print(11111111)
            #words = db.get_words(word)
            #data = [{'value': x[0]} for x in words]
            #data = Clock.schedule_once( db.get_words(word), -1 )
            """words = db.get_words(word)
            print(2222222222)
            data = [{'value': x[0]} for x in words]"""
            #data = db_query(word, db_main)
            data = trie.trie_query(word.lower())
            if self.suggest_autocomplete == 'true' and data:
                self.suggestion_text = str(data[0]["value"])
        else:
            data = []
        #print(data)
        self.app.root.ids.list_words.data = data
        #print(WORD)
        #return data

    def select_word_BACKUP(self):
        ### ci = global cursor; cc = cursor na linha
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

    def select_word(self):
        ci = self.cursor_index()
        text = self.text
        start = max(0, len(text[:ci]) - max(text[:ci].rfind(i) for i in (' ', '\n', '.','!','?', ',',';')))
        end = re.search(r' |\n|\.|\?|!|,|;', text[ci:])
        end = end.span()[0] if end != None else (len(text) - ci)
        self.select_text(ci - start, ci + end)
        value = self.selection_text
        value = re.sub(r' |\.|\?|!|,|;|\n', '', value).strip()
        self.cancel_selection()
        return(value)

    def select_phrase(self):
        ci = self.cursor_index()
        text = self.text
        start = max(0, len(text[:ci]) - max(text[:ci].rfind(i) for i in ('.','!','?','\n')))
        end = re.search(r'\.|\?|!|\n', text[ci:])
        end = end.span()[0] if end != None else (len(text) - ci)
        self.select_text(ci - start, ci + end)
        value = self.selection_text
        value = re.sub(r'\.|\?|!|\\n', '', value).strip()
        self.cancel_selection()
        return(value)

    def select_paragraph(self):
        ci = self.cursor_index()
        text = self.text
        start = max(0, len(text[:ci]) - text[:ci].rfind('\n'))
        end = re.search(r'\n', text[ci:])
        end = end.span()[0] if end != None else (len(text) - ci)
        self.select_text(ci - start, ci + end)
        value = self.selection_text.strip()
        self.cancel_selection()
        return(value)

    def get_antonyms(self, word):
        ant = Dictionary(word, lang=self.lang).antonyms
        ant = list(dict.fromkeys(ant))#remove duplicates
        data = [{'value': x} for x in ant]
        self.app.root.ids.list_antonyms.data = data

    def get_synonyms(self, word):
        syn = Dictionary(word, lang=self.lang).synonyms
        syn = list(dict.fromkeys(syn))#remove duplicates
        data = [{'value': x} for x in syn]
        self.app.root.ids.list_synonyms.data = data

    def updateWord(self, word):
        ### Updates the word at the cursor for a new one
        ci = self.cursor_index()
        text = self.text
        start = max(0, len(text[:ci]) - max(text[:ci].rfind(i) for i in (' ', '\n', '.','!','?',',',';')))
        start -= 1
        end = re.search(r' |\n|\.|\?|!|,|;', text[ci:])
        end = end.span()[0] if end != None else (len(text) - ci)
        self.select_text(ci - start, ci + end)
        value = self.selection_text
        self.delete_selection()
        self.insert_text(word)
        self.cancel_selection()
        #self.focus = True
        #print(self.focus)




    def change_scroll_y(self, text_input, scroll_text):
        y_cursor = text_input.cursor_pos[1]
        y_bar = scroll_text.scroll_y * (text_input.height-scroll_text.height)
        if text_input.height > scroll_text.height:
            if y_cursor >= y_bar + scroll_text.height:
                dy = y_cursor - (y_bar + scroll_text.height)
                scroll_text.scroll_y = scroll_text.scroll_y + scroll_text.convert_distance_to_scroll(0, dy)[1] 
            if y_cursor - text_input.line_height <= y_bar:
                dy = (y_cursor - text_input.line_height) - y_bar
                scroll_text.scroll_y = scroll_text.scroll_y + scroll_text.convert_distance_to_scroll(0, dy)[1] 

    def popup(self):
        print('testeeeeeeeeeee')
        print(self.word)
        #popup = Popup(content=Label(text="I am popup"))
        #popup.open()
