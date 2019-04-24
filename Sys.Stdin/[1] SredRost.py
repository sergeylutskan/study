import sys
rost = []
for line in sys.stdin:
    if line == '\n':
        rost.append(0)
    else:
        rost.append(int(line))
if not any(rost):
    print(-1)
else:
    print(sum(rost)/len(rost))
