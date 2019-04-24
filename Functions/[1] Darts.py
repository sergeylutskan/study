# Darts. Scoring contains a values of rings (inner-ring, outer-ring)

def score(*a):
    global scoring
    if len(a) == 1:
        if a[0] == 'Яблочко':
            return 50
        elif a[0] == 'Зеленое кольцо':
            return 25
    elif len(a) == 2:
        return scoring[a[0]][a[1]]

            
scoring = {'Внутреннее_кольцо':{1:24,2:45},'Внешнее_кольцо':{1:22,2:42}}
print(score("Яблочко"))
