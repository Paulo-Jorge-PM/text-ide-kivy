#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from nltk.corpus import wordnet

#Interface for the wordnet nltk corpura
#Gets synonyms and antonyms of a word

class Dictionary:

    def __init__(self, word, lang='pt-pt'):
        if lang=='pt-pt' or lang=='por':
            self.lang = 'por'
        else:
            self.lang = 'eng'

        self.word = word
        self.syns = wordnet.synsets(self.word, lang=self.lang)
        self.synonyms = []
        self.antonyms = []

        self.synonymsAntonyms()

    def getSynset(self, syn=None):
        if syn:
            return syn.name()
        else:
            return self.syns[0].name()

    def getWord(self, syn=None):
        if syn:
            return syn.lemmas()[0].name()
        else:
            return self.syns[0].lemmas()[0].name()

    def definition(self, syn=None):
        if syn:
            return syn.definition()
        else:
            definitions = []
            for syn in self.syns:
                #print(syn.lemmas(lang="por"))
                definitions.append(syn.definition())
            #return self.syns[0].definition()
            return definitions

    def example(self, syn=None):
        if syn:
            return syn.examples()
        else:
            examples = []
            for syn in self.syns:
                examples.append(syn.examples())
            #self.syns[0].examples()
            return examples

    def similarity(syn1, syn2):
        #Format e.g.: syn1 = wordnet.synset('ship.n.01')
        return syn1.wup_similarity(syn2)

    def synonymsAntonyms(self):
        for syn in self.syns:
            for l in syn.lemmas(lang=self.lang):
                self.synonyms.append(l.name())
                if l.antonyms():
                    for ant in l.antonyms():
                        self.antonyms.append(ant.name())

if __name__ == '__main__':
    main = Dictionary('man', lang='pt-pt')
    #print(main.synonyms)
    #print(main.definition())
    print(main.antonyms)
    #print(main.synonyms)
