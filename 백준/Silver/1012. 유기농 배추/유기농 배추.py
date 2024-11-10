import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(cur):
    for i in range(4):
        nxt = (cur[0] + dr[i], cur[1] + dc[i])
        if nxt in visit:
            visit.remove(nxt)
            dfs(nxt)

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    visit = {tuple(map(int, input().split())) for _ in range(K)}
    worm = 0
    
    while visit:
        worm += 1
        dfs(visit.pop())
    print(worm)