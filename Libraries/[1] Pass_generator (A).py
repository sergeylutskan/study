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

    for i in range(m):
        x = choice(unused)
        pasw = pasw + x
        unused.remove(x)
    
    return pasw
       

def main(n, m):
    ans = []
    for i in range(n):
        ans.append(generate_password(m))
        
    return ans



print("Случайный пароль из 7 символов:", generate_password(7))  
print("10 случайных паролей длиной 15 символов:")  
print(*main(10, 15), sep="\n")
