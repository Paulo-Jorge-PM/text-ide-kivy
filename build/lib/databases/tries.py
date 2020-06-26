#!/usr/bin/env python
# -*- coding: utf-8 -*-

import marisa_trie

class Trie:
    def __init__(self, db_list):
        self.trie = marisa_trie.Trie(self.make_list(db_list))

    def make_list(self, cursor):
        words_list = []
        for word in cursor:
            words_list.append(word[0].lower())
        return words_list

    def trie_query(self, word):
        data = [{'value': x} for x in self.trie.keys(word)]
        return data
