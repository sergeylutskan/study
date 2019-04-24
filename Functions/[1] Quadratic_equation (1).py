# Find roots of quadratic equation

def roots_of_quadratic_equation(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ['all']
            return [c]
        return [-c/b]
    elif b == 0:
        if a == 0:
            if c == 0:
                return ['all']
            return [c]
        return [(-c/a)**0.5,(c/a)**0.5]
    elif c == 0:
        if b == 0:
            if a == 0:
                return ['all']
            return [0]
        return [0,-2*b/2*a]
    else:
        D = b**2 - 4*a*c
        if D < 0:
            return []
        elif D == 0:
            return [-b/2*a]
        else:
            return [(-b-(D)**0.5)/2*a,(-b+(D)**0.5)/2*a]
        


result = roots_of_quadratic_equation(1, -3, 2)
print(*sorted(result))
result = roots_of_quadratic_equation(1, 2, 1)
print(*sorted(result))
