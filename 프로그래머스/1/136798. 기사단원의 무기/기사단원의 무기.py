def solution(N,l,p):
    unit = {n:1 for n in range(1, N+1)}
    for x in range(2, N+1):
        y = 0
        while (y:=y+x) <= N:
            unit[y] += 1
    return sum(p if z > l else z for z in unit.values())