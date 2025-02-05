def solution(s):
    cnt = zero = 0
    while s!="1":
        cnt += 1
        one = 0
        for c in s:
            if c=="0":
                zero += 1
            else:
                one += 1
        s = bin(one)[2:]
    return cnt, zero