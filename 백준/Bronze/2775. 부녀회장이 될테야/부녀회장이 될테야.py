import sys
input = sys.stdin.readline

apart = [[0] * 15 for _ in range(15)]
for i in range(15):
    apart[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        apart[i][j] = apart[i][j-1] + apart[i-1][j]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(apart[k][n])
