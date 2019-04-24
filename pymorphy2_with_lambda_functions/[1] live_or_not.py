# Check the word by animacy. Answer should be in the same number and gender of origin word.

import sys
import pymorphy2

data = list(map(str.strip, sys.stdin))
morph = pymorphy2.MorphAnalyzer()
for word in data:
    if morph.parse(word)[0].tag.POS == 'NOUN':
        number = 'sing' in morph.parse(word)[0].tag.number
        gender = morph.parse(word)[0].tag.gender
        animacy = 'anim' in morph.parse(word)[0].tag.animacy
        if animacy:
            if number and gender == 'femn':
                print('Живая')
            elif number and gender == 'neut':
                print('Живое')
            elif number and gender == 'masc':
                print('Живой')
            elif not number:
                print('Живые')
        else:
            if number and gender == 'femn':
                print('Не живая')
            elif number and gender == 'neut':
                print('Не живое')
            elif number and gender == 'masc':
                print('Не живой')
            elif not number:
                print('Не живые')
    else:
        print('Не существительное')
