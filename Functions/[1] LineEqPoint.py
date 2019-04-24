# Equation of line function by points

def line(s, t):
    x,y = t.split(';')
    s = s.replace('x','*x')
    x = float(x)
    print(str(eval(s)) == str(float(y)))



line("1x+6", "1;7")
line("5x-10", "5;-9")
line("0x+7", "3;7")
line("3.5x+0", "2;7")

