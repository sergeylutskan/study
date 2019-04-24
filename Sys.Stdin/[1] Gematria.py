#find a Gematria of words. Print the sorted list of words by Gematria. if 2 words have the same Gematria, they are sorting in alphabet order.

import sys

string = []
gematry = {}


for line in sys.stdin:
    g = 0
   
    string.append(line.rstrip('\n'))
    for i in string[-1].upper():
        g += ord(i) - ord('A') + 1
    if gematry.get(g) == None:
        gematry[g] = [string[-1]]
    else:
        gematry[g].append(string[-1])

for num in sorted(gematry):
    for word in sorted(gematry[num]):
        print(word)


