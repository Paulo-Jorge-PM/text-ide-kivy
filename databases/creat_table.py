#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import sqlite3

language = 'pt-pt'
db_path = os.path.join('databases', language)
db_get = os.path.join(db_path, 'words.sqlite')
db_save = os.path.join(db_path, 'words_fts5.sqlite')


conn = sqlite3.connect(db_save)


def create_tale(conn):
    #words table full-text-search FTS5 mode
    sql_create_table = """CREATE VIRTUAL TABLE words
                          USING FTS5(id,word,synonym,antonym);"""
    c = conn.cursor()
    c.execute(sql_create_table)

    

def add_entry_query(conn, data):
    sql = """INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, data)
    
    
def export_from_words_to_fts5(db_get):
    db = sqlite3.connect(db_get)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM words')
        
    for row in db:
        try:
            print(row[0])
            print(str(row[0]) + row[1] + "\n\r")
            add_entry(row[0], row[1], '', '')
        except:
            print('ERROOOOOOOOO!')
            

if __name__ == '__main__':
    pass
