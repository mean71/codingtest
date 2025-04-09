from functools import lru_cache
from itertools import permutations

@lru_cache
def isprime(n):
    if n < 2:
        return False
    if n in (2,3,5):
        return True
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        return False
    
    for i in range(5, int(n**0.5)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

def solution(nums):
    set_nums = set()
    for k in range(1, len(nums)+1):
        set_nums |= {int("".join(p)) for p in permutations(nums, k)}
    return sum(isprime(n) for n in set_nums)