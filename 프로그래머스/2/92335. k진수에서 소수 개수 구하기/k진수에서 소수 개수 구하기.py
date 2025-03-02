import re

def isprime(n):
    if n < 2:
        return False
    if n==2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def solution(n:int, k:int) -> int:
    k_n = []
    res = 0
    
    while n:
        k_n.append(str(n%k))
        n //= k
    
    for c in re.split(r"0+", "".join(k_n[::-1])):
        if c:
            res += isprime(int(c))
    
    return res