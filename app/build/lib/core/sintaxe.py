#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

from nltk.data import find
from bllipparser import RerankingParser

from nltk.tree import Tree
from nltk import data


#import spacy
#from stanfordcorenlp import StanfordCoreNLP
#import logging
#from nltk.parse import CoreNLPParser
#from pycorenlp import StanfordCoreNLP

#Other interesting tree parser pt & en: https://github.com/Lynten/stanford-corenlp

class Sintaxe:

    def __init__(self, lang='pt-pt'):
        if lang=='pt-pt' or lang=='por':
            self.lang = 'pt'
        else:
            self.lang = 'en'
        
        self.lang = lang

        #self.text = ''
        self.parser = self.load_parser()
        self.tree = None

    def generate(self, text):
        parsed = self.parse(text)
        tree = Tree.fromstring(parsed)
        self.tree = tree
        return tree

    def parse(self, text):
        return self.parser.simple_parse(text)

    def load_parser(self):
        nltk_data = os.path.join('data', 'nltk_data')
        model = os.path.join(nltk_data, 'models', 'bllip_wsj_no_aux')
        return RerankingParser.from_unified_model_dir(model)

    def draw(self, tree=None):
        if tree:
            tree.draw()
        else:
            self.tree.draw()


    def printTree(self, tree=None):
        if tree:
            tree.pretty_print()
        else:
            self.tree.pretty_print()

if __name__ == '__main__':
    main = Sintaxe('I am testing this new system.', lang='en')
    print(repr(main.tree))
    #main.printTree()
    #main.draw()
