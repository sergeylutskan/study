# Inflect the verb

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

word = input()
if morph.parse(word)[0].tag.POS in {'VERB', 'INFN'}:
    print(morph.parse(word)[0])
    print('Прошедшее время:')
    print(morph.parse(word)[0].inflect({'masc','past'}).word)
    print(morph.parse(word)[0].inflect({'past','femn'}).word)
    print(morph.parse(word)[0].inflect({'past','neut'}).word)
    print(morph.parse(word)[0].inflect({'past','plur'}).word)
    print('Настоящее время:')
    print(morph.parse(word)[0].inflect({'pres','sing','1per'}).word)
    print(morph.parse(word)[0].inflect({'pres','plur','1per'}).word)
    print(morph.parse(word)[0].inflect({'pres','sing','2per'}).word)
    print(morph.parse(word)[0].inflect({'pres','plur','2per'}).word)
    print(morph.parse(word)[0].inflect({'pres','sing','3per'}).word)
    print(morph.parse(word)[0].inflect({'pres','plur','3per'}).word)
else:
    print('Не глагол')

