#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os.path
import sqlite3

#sqlite3 db
class Database:
    def __init__(self, sqlite_file):
        #db_path = os.path.join('databases', language)
        #db_words_path = os.path.join(db_path, 'words.sqlite')

        self.db_words = self.sqlite_connection(sqlite_file)
        self.cursor = self.db_words.cursor()

    def sqlite_connection(self, path):
        return sqlite3.connect(path, check_same_thread=False)

    def words(self):
        return self.cursor.execute('SELECT word FROM words WHERE id > 0')

    def synonyms(self, word):
        return self.cursor.execute('SELECT synonym FROM words WHERE word = ?', (word,))

    def antonyms(self):
        pass
