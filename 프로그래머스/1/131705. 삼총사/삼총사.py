def solution(n):
    ln = len(n)
    count = 0
    for i in range(ln):
        for j in range(i + 1, ln):
            for k in range(j + 1, ln):
                if n[i] + n[j] + n[k] == 0:
                    count += 1
    return count