def solution(arr):
    stk = []
    for n in arr:
        while stk and stk[-1] >= n:
            stk.pop()
        stk.append(n)
    return stk