import sys
from collections import deque
input = sys.stdin.readline

def move_dist(n, m):
    if n==m==1:
        return 1
    visit = deque([(1, 1, True, 1)]) # (r,c,벽부수기 찬스,거리)
    visited = {(1,1,True)}
    adj_map = (["2"*(M+2)] + ["2" + input().strip() + "2" for _ in range(N)] + ["2"*(M+2)])

    while visit:
        r, c, skill, dist = visit.popleft()
        
        for dr, dc in ((1,0), (0,1), (0,-1), (-1,0)):
            nr, nc = r+dr, c+dc
            if nr == N and nc == M:
                return dist+1
            if adj_map[nr][nc] == "2" or (nr, nc, skill) in visited:
                continue
            
            if adj_map[nr][nc] == "0":
                visited.add((nr,nc,skill))
                visit.append((nr, nc, skill, dist+1))
            elif adj_map[nr][nc] =="1" and skill:
                visited.add((nr,nc, False))
                visit.append((nr, nc, False, dist+1))
    return -1

N, M = map(int, input().split()) # 1 <= N,M <= 1000
print(move_dist(N, M))