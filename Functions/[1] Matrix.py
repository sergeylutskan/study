# Creates a matrix with 1,2 or 3 dimensions
# Task for Learining variable numbers of input arguments of function

def matrix(*s):
    buffer = []
    ans = []
    if len(s) == 0:
        return [0]
    elif len(s) == 1:
        for i in range(int(s[0])):
            for j in range(int(s[0])):
                buffer.append(0)
            ans.append(buffer)
            buffer = []
        return ans
    elif len(s) == 2:
        for i in range(int(s[0])):
            for j in range(int(s[1])):
                buffer.append(0)
            ans.append(buffer)
            buffer = []
        return ans
    elif len(s) == 3:
        for i in range(int(s[0])):
            for j in range(int(s[1])):
                buffer.append(int(s[2]))
            ans.append(buffer)
            buffer = []
        return ans

rows = matrix(3,4,5)
for row in rows:
    print(*row)
