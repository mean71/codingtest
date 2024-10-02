def solution(n):
    a=1
    if len(n) >=11:
        return sum(n)
    else:
        for i in n:
            a=a*i
        return a