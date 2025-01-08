def solution(want, num, discount):
    want = {k:v for k,v in zip(want, num)}
    num = 0
    for i in range(len(discount)):
        if discount[i] in want:
            want[discount[i]] -= 1
        if i > 9 and discount[i-10] in want:
            want[discount[i-10]] += 1
        if not any(want.values()):
            num += 1
    return num