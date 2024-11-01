def solution(l,a):
    for i,j in a:
        l[i],l[j] = l[j],l[i]
    return l