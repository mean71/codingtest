def solution(d, budget):
    for i in range(len(d)):
        budget -= sorted(d)[i]
        if budget < 0:
            return i
    return i+1