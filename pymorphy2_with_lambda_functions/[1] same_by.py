# Checks some criterion of values. Criterion is lambda function

def same_by(characteristic, objects):
    result = list(map(characteristic, objects))
    answer = list(map(lambda x: x == result[0], result))
    return all(answer)



values = [2,2,1]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
