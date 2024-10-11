def solution(a,f):
    res = []
    for x,y in enumerate(f):
        if y:
            res.extend([a[x]for _ in range(a[x]*2)])
        else:
            res = res[:len(res)-a[x]]
    return res