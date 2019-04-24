# Convert arab numbers to roman

def roman():
    global one
    global two
    global three
    CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
 
    def arab_to_roman(number):
       if number <= 0: return ''
       ret = ''
       for arab, roman in CONV_TABLE:
           while number >= arab:
               ret += roman
               number -= arab
     
       return ret

    three = '{} + {} = {}'.format(arab_to_roman(one), arab_to_roman(two), arab_to_roman(one + two))
    print(three)

one = 5
two = 4
roman()
