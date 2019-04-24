# Find a 10 NOUNs in text, put it in normal form and sort it by frequency

import sys
import pymorphy2

data = list(map(str.strip, sys.stdin))
morph = pymorphy2.MorphAnalyzer()
words = {}
ans = {}
answer = []

for line in data:
    line = line.replace('.',' ')
    line = line.replace('-',' ')
    line = line.replace('?',' ')
    line = line.replace('!',' ')
    line = line.replace(',',' ')
    line = line.replace(';',' ')
    line = line.replace('(',' ')
    line = line.replace(')',' ')
    line = line.replace('"',' ')
    line = line.replace('[',' ')
    line = line.replace(']',' ')
    line = line.replace('/',' ')
    line = line.replace('\',' ')
    
    for word in line.split():
        m = morph.parse(word.lower())[0]
        
        if m.tag.POS  == 'NOUN' and m.score > 0.5:
            if words.get(m.normal_form):
                words[m.normal_form] += 1
            else:
                words[m.normal_form] = 1
for k,v in words.items():
    if ans.get(v):
        ans[v].append(k)
    else:
        ans[v] = [k]

keys = sorted(ans.keys(), reverse = True)


for k in keys:
        answer = answer + sorted(ans[k], reverse=True)
print(*answer[:10])
