def solution(n, m):
    temp = n*m
    while True:
        if m:
            n,m = m, n%m
        else: break
    m = temp/n
    return [n, m]