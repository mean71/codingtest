import sys
N, M = map(int, sys.stdin.readline().split())
A,B = [],[]
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        A[i][j]+=B[i][j]
for i in A:
    print(*i,end='\n')