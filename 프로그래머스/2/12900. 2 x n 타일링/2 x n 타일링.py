def solution(n):
    a, b = 1, 1
    
    for _ in range(n):
        a, b = a+b, a%1_000_000_007
    
    return b