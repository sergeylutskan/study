# Find words in the text with 3 or more vowels

def print_long_words(text):
    vowel = {'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я', 'a', 'e', 'i', 'o', 'u', 'y'}
    text = text.split()
    ans = []
    for word in text:
        k = 0
        buffer = ''
        for i in word:
            if i in vowel:
                k += 1   
            if i.isalpha():
                buffer += i
        if k > 3:
            ans.append(buffer)
    for i in ans:
       print(i)

print_long_words('Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.')
