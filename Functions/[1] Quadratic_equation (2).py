# Find roots of quadratic equation

def solve(*coefficients):
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
    if len(coefficients) == 3:
        a, b, c = coefficients
        return roots_of_quadratic_equation(a,b,c)
    elif len(coefficients) == 2:
        a = 0
        b, c = coefficients
        return roots_of_quadratic_equation(a,b,c)
    elif len(coefficients) == 1:
        a = 0
        b = 0
        c = coefficients[0]
        return roots_of_quadratic_equation(a,b,c)    
        


print(sorted(solve(1)))
print(sorted(solve(1, -3, 2)))
