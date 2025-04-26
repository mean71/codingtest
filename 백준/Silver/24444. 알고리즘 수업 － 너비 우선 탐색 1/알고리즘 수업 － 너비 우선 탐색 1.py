import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
idj_lst = [[] for _ in range(N+1)]
visited = [0]*(N+1)
visited[R] = 1
visit = deque([R])
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    idj_lst[u].append(v)
    idj_lst[v].append(u)

for r in idj_lst:
    r.sort()

while visit:
    cur = visit.popleft()
    for next in idj_lst[cur]:
        if visited[next]==0:
            cnt += 1
            visited[next] = cnt
            visit.append(next)

print(*visited[1:], sep="\n")