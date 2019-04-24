# Equation of line function

def equation(a, b):
    a = a.split(';')
    b = b.split(';')
    x1 = float(a[0])
    y1 = float(a[1])
    x2 = float(b[0])
    y2 = float(b[1])
    if (x1 - x2) == 0:
        print(0.0)
    else:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k*x2
        if k == 0.0:
            print(b)
        else:
            print(k,b)

equation("0;0", "1;1")
equation("0;0", "0;4")
equation("4;6.9", "-5.2;6.9")
