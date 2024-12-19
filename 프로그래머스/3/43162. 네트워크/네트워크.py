from typing import List

def solution(node: int, connections: List[List[int]]) -> int:
    visit = []
    visited = set()
    count_connect = 0
    
    for n in range(node):
        
        if n not in visited:
            count_connect += 1
            visit.append(n)
            
        while visit:
            cur = visit.pop()
            visited.add(cur)
            
            for i, j in enumerate(connections[cur]):
                    if j and i not in visited:
                        visit.append(i)
    
    return count_connect