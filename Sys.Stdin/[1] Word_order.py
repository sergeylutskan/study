# Just sort list of words in lower case
# Learning to use lambda function and "one-line coding"

string = input().split()
print(*sorted(string, key=lambda x: x.lower()))
