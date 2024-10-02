def solution(x):
    count = 0
    if x==1: return 0
    while x!=1:
        if x%2==0: x/=2
        else: x=x*3+1
        count+=1
        if x==1: return count
        if count==500: return -1