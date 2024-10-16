import sys

N = int(input())
human = {}
for i in range(N):
    man,log = input().split()
    if log=='enter':
        human[man] = 1
    else:
        del human[man]

for xman in sorted(human, reverse=True):
    print(xman)