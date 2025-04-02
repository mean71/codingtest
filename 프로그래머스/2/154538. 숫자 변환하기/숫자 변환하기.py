from collections import deque

def solution(x, y, n):
    visit = deque([(y, 0)])
    visited = set()
    
    while visit:
        cur, cnt = visit.popleft()
        
        if cur == x:
            return cnt
        if cur in visited:
            continue
        visited.add(cur)
        
        if (y:= cur-n) >= x and y not in visited:
            visit.append((y, cnt+1))
        if cur%2 == 0 and (y:= cur//2) >= x and y not in visited:
            visit.append((y, cnt+1))
        if cur%3 == 0 and (y:= cur//3) >= x and y not in visited:
            visit.append((y, cnt+1))
    
    return -1