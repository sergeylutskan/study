#find a comments in Python-code

import sys

print(len(list(filter(lambda x: x[0]=='#', list(map(str.strip, sys.stdin))))))

