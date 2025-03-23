from functools import reduce

def solution(land):
    return max(reduce(lambda a, b: [b[i] + max(a[:i] + a[i+1:]) for i in range(4)], land))