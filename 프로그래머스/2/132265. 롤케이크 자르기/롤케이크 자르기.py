from collections import Counter

def solution(topping):
    right = Counter(topping)
    left = Counter()
    res = 0
    for k in topping:
        left[k] += 1
        right[k] -= 1
        if not right[k]:
            del right[k]
        if len(left) == len(right):
            res += 1
    return res