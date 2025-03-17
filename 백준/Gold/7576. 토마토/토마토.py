import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split()) # 2 <= M,N <= 1000
box = [[-1]*(M+2) for _ in range(N+2)]
visit = deque()
day = 0
dn = ((0,1), (0,-1), (1,0), (-1,0))
zero = 0

for i in range(1, N+1):
    for j, x in enumerate(map(int, input().split()), 1):
        box[i][j] = x
        if x == 1:
            visit.append((i,j,0))
        elif x == 0:
            zero += 1


while visit:
    cur = visit.popleft()
    
    for d in range(4):
        nr, nc = cur[0] + dn[d][0], cur[1] + dn[d][1]
        if box[nr][nc] == 0:
            box[nr][nc] = 1
            zero -= 1
            visit.append((nr, nc, cur[2]+1))
            day = max(day, cur[2]+1)

print(-1 if zero else day)