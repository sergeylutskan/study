def ask_password(login, password, success, failure):
    vowels = set('aeiouy')
    consonants = set(chr(n) for n in range(ord('a'), ord('z') + 1) if chr(n) not in vowels)
    messages = ['', 'WRONG NUMBER OF VOWELS', 'WRONG CONSONANTS', 'EVERYTHING IS WRONG']
    r1 = 0 if sum(1 for c in password if c in vowels) == 3 else 1
    r2 = 0 if [c for c in login if c in consonants] == [c for c in password if c in consonants] else 2
    message = messages[r1 + r2]    
    if message:
        failure(login, message)
    else:
        success(login)
              
def main(login, password):
    def say_hello(login):
        print(f'Привет {login}')
    def report_error(login, message):
        print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {message}.')
    ask_password(login,password,say_hello, report_error)

main("anastasia", "nsyatos")
main("eugene", "aanig")
ask_password("anastasia", "nsyatos", lambda login: print('super'), lambda login, err: print('bad'))
