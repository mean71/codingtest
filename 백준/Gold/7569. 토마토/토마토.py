import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split()) # 2 <= M,N <= 100, 1 <= H <= 100
box = [[[-1]*(M+2) for _ in range(N+2)] for _ in range(H+2)]
visit = deque([])
day, zero = 0, 0
dr, dc, dh = (1,-1,0,0,0,0), (0,0,1,-1,0,0), (0,0,0,0,1,-1)

for i in range(1, H+1):
    for j in range(1, N+1):
        for k, x in enumerate(map(int, input().split()), 1):
            box[i][j][k] = x
            if x==1:
                visit.append((i,j,k,0))
            elif x==0:
                zero += 1

while visit:
    cur = visit.popleft()
    
    for i in range(6):
        nr, nc, nh = cur[0]+dr[i], cur[1]+dc[i], cur[2]+dh[i]
        if box[nr][nc][nh]==0:
            box[nr][nc][nh] = 1
            zero -= 1
            d = cur[3]+1
            visit.append((nr,nc,nh,d))
            day = max(day, d)

print(-1 if zero else day)