import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj_lst = [[] for _ in range(N+1)]

for i, d in enumerate(map(int, input().split()), 1):
    for n in range(i%d, i, d):
        adj_lst[i].append(n)
    for n in range(i+d, N+1, d):
        adj_lst[i].append(n)

start, target = map(int, input().split())
visit = deque([start])
visited = [-1]*(N+1)
visited[start] = 0

while visit:
    cur = visit.popleft()
    
    if cur == target:
        print(visited[cur])
        break
    
    for nxt in adj_lst[cur]:
        if visited[nxt] == -1:
            visited[nxt] = visited[cur] + 1
            visit.append(nxt)
else:
    print(-1)