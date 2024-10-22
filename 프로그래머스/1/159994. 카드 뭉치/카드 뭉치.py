def solution(x,y,G):
    i = j = 0
    for g in G:
        if g == x[i]:
            if i < len(x)-1:
                i += 1
        elif g == y[j]:
            if j < len(y)-1:
                j += 1
        else:
            return 'No'
    else:
        return 'Yes'