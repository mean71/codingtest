def solution(n, m):
    temp = n*m
    while m:
        n,m = m, n%m
    m = temp/n
    return [n, m]