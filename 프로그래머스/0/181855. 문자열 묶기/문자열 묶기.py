from collections import Counter

def solution(l):
    l = Counter(map(len,l))
    return max((v,k) for k,v in l.items())[0]