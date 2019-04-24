# Codes and decodes a Morse code

MorseCode = {'A':'.-',
             'B':'-...',
             'C':'-.-.',
             'D':'-..',
             'E':'.',
             'F':'..-.',
             'G':'--.',
             'H':'....',
             'I':'..',
             'J':'.---',
             'K':'-.-',
             'L':'.-..',
             'M':'--',
             'N':'-.',
             'O':'---',
             'P':'.--.',
             'Q':'--.-',
             'R':'.-.',
             'S':'...',
             'T':'-',
             'U':'..-',
             'V':'...-',
             'W':'.--',
             'X':'-..-',
             'Y':'-.--',
             'Z':'--..'
             }
MorseCodeCyr = {
             'А':'-.',
             'Б':'-...',
             'В':'.--',
             'Г':'--.',
             'Д':'-..',
             'Е':'.',             
             'Ж':'...-',
             'З':'--..',
             'И':'..',
             'Й':'.---',
             'К':'-.-',
             'Л':'.-..',
             'М':'--',
             'Н':'-.',
             'О':'---',
             'П':'.--.',
             'Р':'.-.',
             'С':'...',
             'Т':'-',
             'У':'..-',
             'Ф':'..-.',
             'Х':'....',
             'Ц':'-.-.',
             'Ч':'---.',
             'Ш':'----',
             'Щ':'--.-',
             'Ъ':'--.--',
             'Ы':'-.--',
             'Ь':'-..-',
             'Э':'..-..',
             'Ю':'..--',
             'Я':'-.-.'
             
             }
def encode_to_morse(text,lang):
    Code = ''
    if lang == '1':
        for i in text:
            Code = Code + MorseCodeCyr[i] + ' '
    else:
        for i in text:
            Code = Code + MorseCode[i] + ' '
    return print(Code)

def decode_from_morse(code,lang):
    text = ''
    codesplit = code.split()
    if lang == '1':
        for i in codesplit:
            for k, v in MorseCodeCyr.items():
                if i == v:
                    text = text + k
    else:
        for i in codesplit:
            for k, v in MorseCode.items():
                if i == v:
                    text = text + k                
    return(print(text))
        

    
if __name__ == '__main__':
    a = 5
    while a != '0':
        lang = input('По умолчанию используется латиница.\nЕсли нужно использовать кириллицу - введите цифру 1\n')
        a = input('Вы хотите закодировать (1) или раскодировать (2) информацию?\nВведите только цифру\n')
        if  a == '1':
            encode_to_morse(input('Введите текст для кодирования:\n').upper(),lang)
        elif a == '2':
            decode_from_morse(input('Введите код Морзе для декодирования:\nБуквы должны быть разделены пробелом\n'),lang)
        else:
            print('Неверно введен код, попробуйте еще раз')
            continue
        
        
            
        

