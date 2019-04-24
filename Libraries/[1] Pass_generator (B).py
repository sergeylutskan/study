from random import randint, choice
import string

def generate_password(m):
    letters = list(string.ascii_letters + string.digits)
    letters.remove('0')
    letters.remove('l')
    letters.remove('I')
    letters.remove('1')
    letters.remove('o')
    letters.remove('O')    
    pasw = choice(letters[49:]) + choice(letters[:25]) + choice(letters[25:49])
    if m == 3:
        return pasw
    elif m == 2:
        return pasw[:2]
    elif m == 1:
        return pasw[0]
    elif m < 0:
        return 'Неверное количество символов'
    for i in range(m-3):
        pasw = pasw + choice(letters)
    return pasw
        

def main(n, m):
    ans = []
    for i in range(n):
        ans.append(generate_password(m))
    return ans



print("Случайный пароль из 7 символов:", generate_password(7))  
print("10 случайных паролей длиной 15 символов:")  
print(*main(10, 15), sep="\n")
