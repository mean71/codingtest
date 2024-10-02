def solution(n):
    tmp = ''
    while n:
        tmp += str(n%3)
        n//=3
    return int(tmp, 3)