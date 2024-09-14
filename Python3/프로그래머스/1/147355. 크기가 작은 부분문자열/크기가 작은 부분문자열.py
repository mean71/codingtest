def solution(t, p):
    lp = len(p)
    lst = []

    for i in range(len(t)):
        if len(t[i:i+lp]) ==lp:
            lst.append(''.join(t[i:i+lp]))
    lp=0
    for i in lst:
        if i <= p: lp+=1
    return lp