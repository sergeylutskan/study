# Finds a rythm of word

words = input().split()
vowels = {'а','е','ё','и','о','у','ы','э','ю','я'}
words = list(map(lambda x: list(x), words))
ritm = []
for word in words:
    vow = list(map(lambda x: x in vowels, word))
    ritm.append(vow.count(True))
result = list(map(lambda x: x == ritm[0], ritm))
if all(result):
    print('Парам пам-пам')
else:
    print('Пам парам')

