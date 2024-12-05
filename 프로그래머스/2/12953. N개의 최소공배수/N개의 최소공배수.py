def solution(l):
    max_n = max(l)
    x = 1
    while True:
        mul = max_n*x
        if not sum(mul%n for n in l): break
        x += 1
    return mul