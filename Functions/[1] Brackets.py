# Check all brackets to be closed

def bracket_check(test_string):
    closed_bracket = 0
    open_bracket = 0
    f = True
    for i in test_string:
        if i == ')':
            closed_bracket += 1
        else:
            open_bracket += 1
        if closed_bracket > open_bracket:
            print('NO')
            f = False
            break
    if f:        
        if open_bracket - closed_bracket == 0:
            print('YES')
        else:
            print('NO')


bracket_check('((()))')
bracket_check('()')
bracket_check('(()((')
