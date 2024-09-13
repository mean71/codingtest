def solution(n):
    res = ''
    while n > 0:
        res = res+str(n%3)
        n//=3
    return sum([3**i*int(j) for i,j in enumerate(res[::-1])])