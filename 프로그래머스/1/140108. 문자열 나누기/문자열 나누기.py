def solution(s):
    res = 0
    while s:
        res += 1
        x, xn = s[0], 1
        for i, c in enumerate(s[1:]):
            xn += 1 - 2*(x!=c)
            if 0 == xn:
                s = s[i+2:]
                break
        else: break
    return res