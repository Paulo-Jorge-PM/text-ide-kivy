#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

class Statistics:

    def __init__(self, lang='pt-pt'):

        if lang=='pt-pt' or lang=='por':
            self.lang = 'pt'
        else:
            self.lang = 'en'

    def countCharacters(self, text):
        characters = len(text.strip())
        return str(characters)

    def countWords(self, text):
        temp = text
        while temp.find('  ') != -1:
            print(temp.find('  '))
            temp = temp.replace('  ', ' ')
        words = len(temp.strip().split())
        return str(words)

    def countParagraphs(self, text):
        temp = text.strip()
        while temp.find('\n\n') != -1:
            temp = temp.replace('\n\n', '\n')
        paragraphs = temp.count('\n')
        return str(paragraphs+1)

    def countPhrases(self, text):
        phrases = len(re.findall(r'\.\s\w|\?\s\w|!\s\w', text ))
        phrases = '1' if (phrases == 0 and text != '') else '0' if text=='' else str(phrases+1)
        return str(phrases)

if __name__ == '__main__':
    main = Statistics('pt-pt')
    print(main.countWords('Testando o funcionamento do countador.'))
