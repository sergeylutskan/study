# Originally it was code with mistakes and I have to correct it


def continue_fibonacci_sequence(s, n): #заменен аргумент sequence на аргумент s
    global sequence #добавлено указание на глобальную переменную
    for i in range(n): 
        next_element = sequence[-1] + sequence[-2] 
        sequence = sequence + [next_element]
    return sequence #добавлена функция возврата значения последовательности

sequence = [1,1,2]
continue_fibonacci_sequence(sequence, 0)
print(*sequence)
