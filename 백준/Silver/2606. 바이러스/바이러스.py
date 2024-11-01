import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
E = int(input())
adj_lst = [[] for _ in range(V+1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)

queue_stack = deque([1]) # 예정지 1번
visited = set([1]) # 방문지 1번

while queue_stack:
    cur = queue_stack.pop() # stack FS
    
    for nxt in adj_lst[cur]:
        if nxt not in visited:
            queue_stack.append(nxt)
            visited.add(nxt)
print(len(visited)-1)