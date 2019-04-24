# Function ask the name first and then calling user by name.

def polite_input(question):
    global name
    if name == '':
        name = input('Как Вас зовут?\n')
    answer = input(name + ', ' + question + '\n')
    return answer

name = ''
age = polite_input('укажите возраст')
school_number = polite_input('укажите номер школы')
class_num = polite_input('укажите полный номер класса')
