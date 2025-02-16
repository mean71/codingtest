from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    maps = [[0]*(m + 2)] + [[0] + r + [0] for r in maps] + [[0]*(m + 2)]
    visit = deque([(1,1,1)])
    visited = {(1,1)}
    
    while visit:
        r, c, cnt = visit.popleft()
        if r == n and c == m:
            return cnt
        
        for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
            nr, nc = r + dr, c + dc
            if maps[nr][nc] and (nr, nc) not in visited:
                visit.append((nr, nc, cnt+1))
                visited.add((nr, nc))
    else:
        return -1