#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import sqlite3

def create_tale(conn):
    #words table full-text-search FTS5 mode
    sql_create_table = """CREATE VIRTUAL TABLE words
                          USING FTS5(id,word,synonym,antonym);"""
    c = conn.cursor()
    c.execute(sql_create_table)
    print("DB CREATED!")

    

def add_entry(conn, data):

    sql = """INSERT INTO words(id,word,synonym,antonym)
              VALUES(?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        print("Inserting", data)
    except:
        print("Errrrrrrrrrrrrro no add_entry")
    
def export_from_words_to_fts5(conn, db_get):
    print("START")
    db = sqlite3.connect(db_get)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM words')
    
    print("START GET FROM WORDS")    
    for row in cursor:
        try:
            #print(str(row[1]) + "\n\r")
            add_entry(conn, (row[0], row[1], '', ''))
        except:
            print('ERROOOOOOOOO!')
            print(str(row[1]))

if __name__ == '__main__':

    language = 'pt-pt'
    db_path = os.path.join('databases', language)
    db_get = os.path.join(db_path, 'words.sqlite')
    db_save = os.path.join(db_path, 'words_fts5.sqlite')
    
    conn = sqlite3.connect(db_save)
    
    create_tale(conn)
    export_from_words_to_fts5(conn, db_get)
    
    conn.commit()
    conn.close()
