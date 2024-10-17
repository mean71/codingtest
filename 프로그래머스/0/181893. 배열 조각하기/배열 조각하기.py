def solution(a,q):
    for i,j in enumerate(q):
        if i%2:
            a=a[j:]
        else:
            a=a[:j+1]
    return a