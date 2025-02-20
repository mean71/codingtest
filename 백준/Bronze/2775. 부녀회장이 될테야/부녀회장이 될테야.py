import sys
input = sys.stdin.readline

apart = [list(range(15)) for _ in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        apart[i][j] = apart[i][j-1] + apart[i-1][j]

for _ in range(int(input())):
    k, n = int(input()), int(input()) # 1<=k,n<=14
    print(apart[k][n])
