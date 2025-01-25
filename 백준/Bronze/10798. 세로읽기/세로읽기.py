import sys

string = [(sys.stdin.readline().strip()) for _ in range(5)]
strs = ''
L = max(map(len, string))

for i in range(L):
    for j in range(5):
        if i < len(string[j]):
            strs += string[j][i]
print(strs)