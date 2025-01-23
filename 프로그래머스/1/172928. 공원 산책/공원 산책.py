def solution(park, routes):
    park_xy = [[False]*(2 + len(park[0])) for _ in range(2 + len(park))]
    d = {"N":(-1,0),"S":(1,0),"E":(0,1),"W":(0,-1)}
    
    for r,pr in enumerate(park):
        for c ,pc in enumerate(pr):
            if pc=="S":
                dog = r+1, c+1
            park_xy[r+1][c+1] = pc!="X"
    
    for direction, move in map(lambda x:x.split(), routes):
        dr, dc = d[direction]
        for n in range(1, int(move)+1):
            nr, nc = dog[0] + dr*n, dog[1] + dc*n
            if not park_xy[nr][nc]:
                break
        else:
            dog = nr, nc
    
    return dog[0]-1, dog[1]-1