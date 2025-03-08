import sys
input = sys.stdin.readline

n = []

for i in range(1, int(input())+1):
    x, y, v = map(int, input().split())
    n.append(((x**2 + y**2)**0.5/v, i))

n.sort()

for i in n:
    print(i[1])