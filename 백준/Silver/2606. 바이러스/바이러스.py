import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
E = int(input())
adj_lst = [[] for _ in range(N+1)]
visit = deque([1])
visited = set([1])

for _ in range(E):
    s, e = map(int, input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)

while visit:
    cur = visit.pop()
    
    for nxt in adj_lst[cur]:
        if nxt not in visited:
            visit.append(nxt)
            visited.add(nxt)
            
print(len(visited)-1)