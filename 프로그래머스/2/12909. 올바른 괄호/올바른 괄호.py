'''solution=lambda s:(lambda x:x[-1]==0 and all(y > -1 for y in x))([sum(1 if e=='('else-1 for e in s[i-len(s)::-1]) for i in range(len(s))])'''
def solution(s):
    res = 0
    for c in s:
        res += 1 - 2*(c == ")")
        if res < 0:
            return False
    return True and not res