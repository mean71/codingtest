def solution(l,a):
    for i,j in a:
        l.insert(i, l.pop(j))
        l.insert(j, l.pop(i+1))
    return l
# for i,n in enumerate(l):
    