def solution(n):
    a,b = 1,1
    for _ in range(n-1):
        a,b = a+b, a
    return a%1234567