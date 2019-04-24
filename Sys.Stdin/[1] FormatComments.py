#Find comments in Python-code, print the number of Line with comment and comment without "#"

import sys

data = list(map(str.strip, sys.stdin))
comments = list(filter(lambda x: x[0]=='#', data))
for comment in comments:
    print('Line ' + str(data.index(comment) + 1) + ':' + comment.strip('#'))
