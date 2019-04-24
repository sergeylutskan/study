from random import randint, choice
import string

def chars():
    letters = set(string.ascii_letters + string.digits)
    letters.remove('0')
    letters.remove('l')
    letters.remove('I')
    letters.remove('1')
    letters.remove('o')
    letters.remove('O')
    return list(letters)

def generate_password(m):
    pasw = ''
    for i in range(m):
        pasw = pasw + choice(chars())
    return pasw

def main(n, m):
    ans = []
    pasw = ''
    for i in range(n):
        pasw = ''
        for j in range(m):
            pasw = pasw + choice(chars())
        ans.append(pasw)
    return ans



print("Случайный пароль из 7 символов:", generate_password(7))  
print("10 случайных паролей длиной 15 символов:")  
print(*main(10, 15), sep="\n")
