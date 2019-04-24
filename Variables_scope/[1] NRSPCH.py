def translate(text):
    global translatedText
    pool = ('а','у','е','ы','о','э','я','и','ю','ё','А','Б','Е','Ы','О','Э','Я','И','Ю','Ё','.',',','!','?',':','-')
    text = text.split()
    ans = ''
    for word in text:
        w = ''
        for i in word:
            if i in pool:
                pass
            else:
                w = w + i
        ans = ans + w + ' '
    translatedText = ' '.join(ans.split())

translatedText = None
text = 'Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.'
translate(text)
print(translatedText)
