def solution(l):
    lst = [i for i in map(lambda x: set(range(x[0],x[1])), l)]
    res = lst[2]&lst[1]
    res.update(lst[1]&lst[0])
    res.update(lst[2]&lst[0])
    return len(res)