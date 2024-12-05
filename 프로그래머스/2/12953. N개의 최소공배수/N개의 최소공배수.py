# solution=lambda L:(m:=max(L))and next(i for i in range(m,m**m+1,m)if all(i%j==0 for j in L))

def solution(L):
    m = max(L)
    for mul in range(m, m**m+1, m):
        if all(mul%n==0 for n in L):
            return mul