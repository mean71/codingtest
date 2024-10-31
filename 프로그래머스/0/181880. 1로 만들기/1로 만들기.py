def solution(l):
    c = 0
    for n in l:
        while n > 1:
            n //= 2
            c += 1
    return c