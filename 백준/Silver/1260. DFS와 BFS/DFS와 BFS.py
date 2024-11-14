import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj_lst[s].append(e)    # extend -> append로 수정
    adj_lst[e].append(s)

# 각 정점의 인접 리스트 정렬
for i in range(N+1):
    adj_lst[i].sort()

def dfs(start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        cur = stack.pop()
        if cur not in visited:
            visited.add(cur)
            result.append(cur)
            for nxt in sorted(adj_lst[cur], reverse=True):
                if nxt not in visited:
                    stack.append(nxt)
    return result

def bfs(start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        cur = queue.popleft()
        result.append(cur)
        
        for nxt in adj_lst[cur]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return result

print(*dfs(V))
print(*bfs(V))