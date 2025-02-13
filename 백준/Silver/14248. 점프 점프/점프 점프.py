import sys
input = sys.stdin.readline

N = int(input())
adj_lst = [[] for _ in range(N+1)]

for i, d in enumerate(map(int, input().split()), 1):
    if i+d <= N:
        adj_lst[i].append(i+d)
    if i-d >= 1:
        adj_lst[i].append(i-d)

visit = [int(input())]
visited = set()

while visit:
    cur = visit.pop()
    visited.add(cur)
    
    for nxt in adj_lst[cur]:
        if nxt not in visited:
            visit.append(nxt)

print(len(visited))