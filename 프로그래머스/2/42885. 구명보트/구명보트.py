'''def solution(P, L):
    P = sorted(P)
    s, e = 0, len(P)-1
    res = len(P)
    
    while s < e:
        boat = P[e]
        while (boat := boat + P[s]) <= L:
            s += 1
            res -= 1
        e -= 1
        
    return res'''

def solution(P, L):
    P = sorted(P)
    s, e = 0, len(P)-1
    res = len(P)
    
    while s < e:
        if P[e] + P[s] <= L:
            s += 1
            res -= 1
        e -= 1
        
    return res