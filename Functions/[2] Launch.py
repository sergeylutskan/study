# Find a sum of daily_food

daily_food = [0,150,160] #массив, обозначающий количество денег, потраченный 

def count_food(days): #создаем функцию count_food с аргументом days
    sum = 0 #создаем локальную переменную sum = 0
    global daily_food #делаем ссылку на глобальную переменную daily_food
    for i in days: #запускаем цикл из элементов переданного аргументв days
        sum += daily_food[i - 1] #вычисляем сумму потраченных средств на питание по дням.
                                 #i-1 необходимо из-за того, что нумерация в массиве начинается с 0
    return sum #возвращаем значение переменной sum

print(count_food([2,3])) #выводим на печать результат работы функции от массива [2,3]
