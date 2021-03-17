#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sqlite3

class Databases():

    def __init__(self):
        language = 'pt-pt'
        db_path = os.path.join('databases', language)
        db_words = os.path.join(db_path, 'words.sqlite')

        #check_same_thread=False can corrupt data if multiple threads write at same time. Usually you should put this in the get_words func so each new thread makes a different connection. But since we only read here, to make it easy I choosed this path
        self.db = sqlite3.connect(db_words, check_same_thread=False)

        #words = self.db.cursor().execute('SELECT word FROM words')

        #self.words = []

        #for word in words:
        #    self.words.append(word)

        #self.cursor = self.db.cursor()
        #self.cursor = cursor

    #cursor.execute('''SELECT word FROM words''')
    #rows = cursor.fetchall()
    #db.close()

    #dbs_tables = ['words', 'morphology']

    #words = ['paulo', 'pauta', 'pausa', 'poeta', 'poente']
    #synonyms = []
    #antonymis = []

    def get_words(self, word):
        cursor = self.db.cursor()
        cursor.execute('SELECT word FROM words WHERE word LIKE ? limit 500', (word+'%',))
        #rows = cursor.fetchall()
        #data = [{'value': x[0]} for x in cursor]
        #data = [{'value':'teste'}]
        #data = [{'value': x[0]} for x in self.words if x[0].startswith(word)]
        #data = [{'value': x} for x in list(word)]
        print(333)
        print(word)
        return cursor

    def dbs_list(self):
        pass

    def words_db(self):
        pass

    def connect_db(self):
        pass
