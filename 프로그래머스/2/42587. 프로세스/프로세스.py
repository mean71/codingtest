from collections import deque

def solution(priorities, location):
    q = deque([(i, p) for i, p in enumerate(priorities)])
    priorities.sort(reverse=True)
    cnt = 0
    
    while q:
        i, p = q.popleft()
        
        if p == priorities[cnt]:
            cnt += 1
            if i == location:
                return cnt
        else:
            q.append((i,p))