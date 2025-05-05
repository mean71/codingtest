import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
painting = ["0"*(n+2)] + ["0"+input()+"0" for _ in range(n)] + ["0"*(n+2)]
visited = [[False]*(n+2)] + [[False]+[True]*n+[False] for _ in range(n)] + [[False]*(n+2)]
Rg_visited = [[False]*(n+2)] + [[False]+[True]*n+[False] for _ in range(n)] + [[False]*(n+2)]
cnt1 = cnt2 = 0
visit = deque()

for i in range(1, n+1):
    for j in range(1, n+1):
        if visited[i][j]:
            visited[i][j] = False
            visit.append((i,j))
            cnt1 += 1
            
            while visit:
                r, c = visit.popleft()
                for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    nr, nc = r+dr, c+dc
                    if visited[nr][nc] and painting[nr][nc] == painting[r][c]:
                        visited[nr][nc] = False
                        visit.append((nr,nc))
        
        if Rg_visited[i][j]:
            Rg_visited[i][j] = False
            visit.append((i,j))
            cnt2 += 1
            
            while visit:
                r, c = visit.popleft()
                for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    nr, nc = r+dr, c+dc
                    if Rg_visited[nr][nc] and (
                        "B"==painting[nr][nc] == painting[r][c] or
                        painting[nr][nc] in "RG" and painting[r][c] in "RG"
                        ):
                        Rg_visited[nr][nc] = False
                        visit.append((nr,nc))

print(cnt1, cnt2)