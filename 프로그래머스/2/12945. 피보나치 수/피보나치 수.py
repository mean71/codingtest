def solution(n):
    assert n >= 0, 'n >= 0'
    a,b = 0,1
    if n == 2:
        a = 1
    for i in range(n):
        a,b = b%1234567,(a+b)%1234567
    return a