# After call setup_profile another functions will know name and days of vacation 

def setup_profile(name, vacationDates):
    global n, d
    n = name
    d = vacationDates
def print_application_for_leave():
    return print('Заявление на отпуск в период '+ d +'. ' + n)
def print_holiday_money_claim(amount):
    print('Прошу выплатить ' + amount + ' отпускных денег. ' + n)
def print_attorney_letter(toWhom):
    return print('На время отпуска в период '+ d +' моим заместителем назначается ' + toWhom + '. ' + n)



setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")
