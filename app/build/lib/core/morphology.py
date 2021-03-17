#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pprint

import nltk
from nltk import pos_tag, word_tokenize, data, sent_tokenize, tokenize
from nltk.lm import MLE
from collections import Counter

import nlpnet

#Config NLTK base data dir corpus pre downloaded, so the user don't need to download it
# baseDir = os.path.dirname(__file__)
# nltk_data = os.path.join(baseDir, 'nltk_data')
# data.path.append(nltk_data)

#from libraries.nltkTaggerPortuguese import tagger

class Morphology:

    def __init__(self, text, lang='pt-pt'):
        if lang=='pt-pt' or lang=='por':
            self.lang = 'pt'
        else:
            self.lang = 'en'

        self.text = text
        self.tokens = self.tokenize(text)
        self.tags = self.tagging()

    def tokenize(self, text):
        if self.lang == 'pt':
            tokens = tokenize.word_tokenize(text, language='portuguese')    
        else:
            tokens = word_tokenize(text)
        return tokens

    def tagging(self):
        if self.lang == 'pt':
            model_path = os.path.join('data', 'pos-pt')
            tagger = nlpnet.POSTagger(model_path, language='pt')
            tags = tagger.tag(self.text)
            #tags = tags.arg_structures
            #tokens = tags.tokens
        else:
            tags = nltk.pos_tag(self.tokens)
        return tags

    def getProperNouns(self, taggedText):
        properNouns = []
        i = 0
        while i < len(taggedText):
            if taggedText[i][1] == 'NNP':
                if taggedText[i+1][1] == 'NNP':
                    properNouns.append(taggedText[i][0].lower() +
                                        " " + taggedText[i+1][0].lower())
                    i+=1 # extra increment added to the i counter to skip the next word
                else:
                    properNouns.append(taggedText[i][0].lower())
            i+=1 # increment the i counter
        return properNouns

    def summarizeText(self, properNouns, topNum):
        '''
        Counts and agreggates the data. TopNum is a int e.g. 100
        '''
        counts = dict(Counter(properNouns).most_common(topNum))
        return counts

    def printNouns(self, nouns=None):
        #if nouns == None:#this if allows it to work without invoking all the class
        #    nouns = self.nouns
        p = pprint.PrettyPrinter(indent=4)
        p.pprint(nouns)

    def gramFrequency(self, text, word1, word2):
        n = 3
        tokenized_text = [list(map(str.lower, word_tokenize(sent))) for sent in sent_tokenize(text)]
        #tokenized_text = self.tokens
        train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)
        model = MLE(n)
        model.fit(train_data, padded_sents)
        print(model.counts[[word1]][word2])

    # def tagPt(self, text):
    #    tagger = pickle.load(open("tagger.pkl"))
    #    portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")
    #    sentences = portuguese_sent_tokenizer.tokenize(text)
    #    tags = [tagger.tag(nltk.word_tokenize(sentence)) for sentence in sentences]
    #    return tags

if __name__ == '__main__':
    main = Morphology('Olá, eu chamo-me Paulo, a vida ter-se-á iniciado há milénios e dese então nem um só dia passsou sem sol e chuva, sem pó e cruz. Tamanha é a sede.', lang='pt-pt')
    print(main.tokens)
    print(main.tags)
