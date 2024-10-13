def solution(n):
    a = [[0 for _ in range(n)] for _ in range(n)]
    mode = [0,1]
    r,c = 0,0
    for x in range(1,n*n+1):
        if mode==[0,1]:
            try:
                if a[r][c+1]:
                    mode=[1,0]
            except:
                mode=[1,0]
        elif mode==[1,0]:
            try:
                if a[r+1][c]:
                    mode=[0,-1]
            except:
                mode=[0,-1]
        elif mode==[0,-1]:
            try:
                if a[r][c-1]:
                    mode=[-1,0]
            except:
                mode=[-1,0]
        elif mode==[-1,0]:
            try:
                if a[r-1][c]:
                    mode=[0,1]
            except:
                mode=[0,1]
        a[r][c]=x
        r += mode[0]
        c += mode[1]
    return a