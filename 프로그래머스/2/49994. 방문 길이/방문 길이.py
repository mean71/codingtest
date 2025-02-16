def solution(dirs):
    D = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
    visited = set()
    cur = 0, 0
    
    for d in dirs:
        dr, dc = D[d]
        nr, nc = cur[0] + 2*dr, cur[1] + 2*dc
        
        if -10 <= nr <= 10 and -10 <= nc <= 10:
            visited.add((cur[0]+dr, cur[1]+dc))
            cur = nr, nc
        
    return len(visited)