# inflects the noun

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

word = input()
if morph.parse(word)[0].tag.POS == 'NOUN':
    print('Единственное число:')
    print('Именительный падеж:', morph.parse(word)[0].inflect({'nomn'}).word)
    print('Родительный падеж:', morph.parse(word)[0].inflect({'gent'}).word)
    print('Дательный падеж:', morph.parse(word)[0].inflect({'datv'}).word)
    print('Винительный падеж:', morph.parse(word)[0].inflect({'accs'}).word)
    print('Творительный падеж:', morph.parse(word)[0].inflect({'ablt'}).word)
    print('Предложный падеж:', morph.parse(word)[0].inflect({'loct'}).word)
    print('Множественное число:')
    print('Именительный падеж:', morph.parse(word)[0].inflect({'nomn','plur'}).word)
    print('Родительный падеж:', morph.parse(word)[0].inflect({'gent','plur'}).word)
    print('Дательный падеж:', morph.parse(word)[0].inflect({'datv','plur'}).word)
    print('Винительный падеж:', morph.parse(word)[0].inflect({'accs','plur'}).word)
    print('Творительный падеж:', morph.parse(word)[0].inflect({'ablt','plur'}).word)
    print('Предложный падеж:', morph.parse(word)[0].inflect({'loct','plur'}).word)
else:
    print('Не существительное')
