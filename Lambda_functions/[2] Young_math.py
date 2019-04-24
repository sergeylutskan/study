# Mini-calculator

def arithmetic_operation(operator):
    if operator == '+':
        return lambda a,b : a+b
    elif operator == '-':
        return lambda a,b : a-b
    elif operator == '/':
        return lambda a,b : a/b
    elif operator == '*':
        return lambda a,b : a*b

operation = arithmetic_operation('+')
print(operation(1, 4))
