def solution(k,s):
    if k >= len(s):
        return [min(s[:i]) for i in range(1,len(s)+1)]
    lst = sorted(s[:k])
    res = [min(s[:i]) for i in range(1,k+1)]
    for x in s[k:]:
        if lst[0] > x:
            res.append(lst[0])
        else:
            lst.append(x)
            lst.sort()
            lst = lst[1:]
            res.append(lst[0])
    return res