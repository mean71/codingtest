import sys
input = sys.stdin.readline
N = int(input())
human = set()
for i in range(N):
    man,log = input().split()
    if log=='enter':human.add(man)
    else:human.discard(man)
for xman in sorted(list(human), reverse=True):
    print(xman)