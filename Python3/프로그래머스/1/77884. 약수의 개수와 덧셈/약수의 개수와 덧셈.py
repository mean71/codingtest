def solution(l,r):
    res = 0
    for i in range(l,r+1):
        measure = {'count':0}
        for j in range(i):
            if not i%(j+1):
                measure['count']+=1
                print(i,j)
        if measure['count']%2:
            res-=i
        else:
            res+=i
    return res