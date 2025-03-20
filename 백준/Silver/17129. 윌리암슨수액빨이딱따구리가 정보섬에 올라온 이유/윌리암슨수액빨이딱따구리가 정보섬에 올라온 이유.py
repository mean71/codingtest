import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 1 <= N,M <= 3000, 4 <= n*m <= 9*10^6
island = [[1]*(M+2) for _ in range(N+2)] # 0:복도, 1:장애물, 2:식구, 3:국장, 4:스시, 5:맥치즈
visit = deque()

for i in range(1, N+1):
    r = input().strip()
    for j, n in enumerate(map(int, r), 1):
        island[i][j] = n
        if n == 2:
            island[i][j] = 1
            visit.append((i, j, 1))

while visit:
    x, y, cnt = visit.popleft()
    
    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
        nx, ny = x+dx, y+dy

        if island[nx][ny] == 0:
            island[nx][ny] = 1
            visit.append((nx, ny, cnt+1))
        
        elif island[nx][ny] in {3, 4, 5}:
            print("TAK")
            print(cnt)
            break
    else:
        continue
    break
else:
    print("NIE")