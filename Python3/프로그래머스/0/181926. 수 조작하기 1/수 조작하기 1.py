def solution(n, control):
    for i in range(len(control)):
        if control[i] == 'w':
            n += 1
        if control[i] == 's':
            n -= 1
        if control[i] == 'd':
            n += 10
        if control[i] == 'a':
            n -= 10
    return n