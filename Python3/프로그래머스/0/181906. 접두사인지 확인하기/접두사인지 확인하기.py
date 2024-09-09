def solution(x,y):
    for i in range(len(y)):
        if y[i] != x[i] or len(y)>len(x): return 0
    return 1