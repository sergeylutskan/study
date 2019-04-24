# make_agree_with_number from PyMorphy2

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

bottle = morph.parse('бутылка')[0]



for i in range(99,0,-1):
    print('В холодильнике', i, bottle.make_agree_with_number(i).word, 'кваса.')
    print('Возьмём одну и выпьем.')
    if (i-1) % 10 == 1 and (i-1) != 11:
        print('Осталась', i-1, bottle.make_agree_with_number(i-1).word, 'кваса.')
    else:
        print('Осталось', i-1, bottle.make_agree_with_number(i-1).word, 'кваса.')
 

