import re

def solution(n:int, k:int) -> int:
    k_n = []
    res = 0
    
    while n:
        k_n.append(str(n%k))
        n //= k
    
    for c in re.split(r"0+", "".join(k_n[::-1])):
        if c in "1":
            continue
        c = int(c)
        
        if c == 2:
            res += 1
            continue
        
        if c%2 == 0:
            continue
        
        for i in range(3, int(c**0.5) + 1, 2):
            if c%i == 0:
                break
        else:
            res += 1
    
    return res