def simple_map(transformation, values):
    global operation
    return map(operation,values)


values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))
