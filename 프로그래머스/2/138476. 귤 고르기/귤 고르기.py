def solution(k,L):
    count = {}
    for n in L: count[n] = 1 + count.get(n, 0)
    count = sorted(count.values(), reverse=True)
    
    temp = 0
    return next(i+1 for i,n in enumerate(count) if (temp:=temp+n) >= k)