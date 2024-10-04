def solution(a,b,n):
    res = 0
    while n >= a:
        res,n = (lambda x,y:(res+x*b,x*b+y))(*divmod(n,a))
    return res