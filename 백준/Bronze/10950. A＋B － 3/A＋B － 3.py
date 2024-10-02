T=int(input())
while T > 0:
    A,B = map(int,input().split())
    if A>0 and B>0:
        print(A+B)
    else:
        continue
    T-=1