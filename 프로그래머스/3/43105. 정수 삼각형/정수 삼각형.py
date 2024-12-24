def solution(t):
    for i in range(len(t) - 1, 0, -1):
        for j in range(len(t[i-1])):
            t[i-1][j] += t[i][j + (t[i][j] < t[i][j+1])]
    return t[0][0]