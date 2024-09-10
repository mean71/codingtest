def solution(n):
    count = 0
    for i in range(n):
        sumnum = 0
        for j in range(1+i,n+1):
            sumnum += j
            if sumnum > n:
                break
            if sumnum == n:
                count += 1
    return count