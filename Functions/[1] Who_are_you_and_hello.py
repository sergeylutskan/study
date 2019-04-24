# Tests the input and say Hello if name is correct

def who_are_you_and_hello():
    name = input()
    if name.isalpha() and name[0].isupper() and name[1:].islower() and name.count(' ') == 0:
        print('Привет, ' + name + '!')
    else:
        who_are_you_and_hello()


who_are_you_and_hello()
