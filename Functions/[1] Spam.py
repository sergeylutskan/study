# Function with default arguments - simple mail

def mail(email=None,name=None,date=None,place='Москва'):
    return 'To: ' + email +'\nЗдравствуйте, '+ name + '!\nБыли бы рады видеть вас на встрече начинающих программистов в ' + place + ', которая пройдет ' + date +'.'

print(mail(email='123@mail.ru',name='Василий',date='25 сентября 2019 года',place='Санкт-Петербург'))
