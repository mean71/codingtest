def solution(want, n, discount):
    want = {k:-v for k,v in zip(want, n)}
    n = 0
    for k in discount[:10]:
        if k in want:
            want[k] += 1
        if not any(want.values()):
            n += 1
    for i in range(len(discount)-10):
        if discount[i] in want:
            want[discount[i]] -= 1
        if discount[i+10] in want:
            want[discount[i+10]] += 1
        if not any(want.values()):
            n += 1
    return n