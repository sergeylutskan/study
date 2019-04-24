# Finds the verbs in text from set

import pymorphy2
import sys

morph = pymorphy2.MorphAnalyzer()

data = list(map(str.strip, sys.stdin))

k = 0
for line in data:
    line = line.replace('.',' ')
    line = line.replace('-',' ')
    line = line.replace('?',' ')
    line = line.replace('!',' ')
    line = line.replace(',',' ')
    line = line.replace(';',' ')
    line = line.replace(':',' ')
    for word in line.split():
        verb = morph.parse(word.lower())[0].tag.POS in {'VERB', 'INFN'}
        
        inf = morph.parse(word.lower())[0].normal_form in {'видеть', 'увидеть', 'глядеть', 'примечать', 'узреть'}
        if verb and inf:
            k += 1
print(k)
