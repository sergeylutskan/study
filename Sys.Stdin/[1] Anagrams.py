n = int(input())
words = []
ans = []
answer = []
for i in range(n):
    words.append(input().lower())
for word1 in words:
    buffer = [word1]
    for word2 in words:
        if all(map(lambda x: x in list(word2) and word1 != word2 and len(word1) == len(word2),word1)):
            buffer.append(word2)
            ans = ans + [buffer]

wordlist = list(map(lambda x: sorted(x),ans))

for w in wordlist:
    answer.append(w)
    while wordlist.count(w) > 1:
        wordlist.remove(w)
for i in map(lambda x: x, list(map(lambda x: x,sorted(answer)))):
    print(*i)

