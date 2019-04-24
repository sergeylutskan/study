from random import randint, choice
import string

def generate_password(m):
    pasw = ''
    unused = list(string.ascii_letters + string.digits)
    unused.remove('0')
    unused.remove('l')
    unused.remove('I')
    unused.remove('1')
    unused.remove('o')
    unused.remove('O')
    a = choice(unused[49:])
    b = choice(unused[:25])
    c = choice(unused[25:49])
    pasw = a + b + c
    unused.remove(a)
    unused.remove(b)
    unused.remove(c)
    if m == 3:
        return pasw
    elif m == 2:
        return pasw[:2]
    elif m == 1:
        return pasw[0]
    elif m < 0:
        return 'Неверное количество символов'
    for i in range(m-3):
        x = choice(unused)
        pasw = pasw + x
        unused.remove(x)
    
    return pasw
       

def main(n, m):
    ans = []
    for i in range(n):
        pasw = generate_password(m)
        ans.append(pasw)
        
    return ans



print("Случайный пароль из 7 символов:", generate_password(7))  
print("10 случайных паролей длиной 15 символов:")  
print(*main(10, 15), sep="\n")
