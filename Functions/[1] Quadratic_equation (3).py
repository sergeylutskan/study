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
    if len(coefficients[0]) == 3:
        a = coefficients[0][0]
        b = coefficients[0][1]
        c = coefficients[0][2]
        
        return roots_of_quadratic_equation(int(a),int(b),int(c))
    elif len(coefficients[0]) == 2:
        a = 0
        b = coefficients[0][0]
        c = coefficients[0][1]
        return roots_of_quadratic_equation(int(a),int(b),int(c))
    elif len(coefficients[0]) == 1:
        a = 0
        b = 0
        c = coefficients[0][0]
        return roots_of_quadratic_equation(int(a),int(b),int(c))    
        


print(*sorted(solve(input().split())))
