def int2base(n, base):
    if n==0:
        return "0"
    
    nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = []
    
    while n:
        num.append(nums[n%base])
        n //= base
    return num[::-1]


def solution(n:int, t:int, m:int, p:int) -> str:
    '''m명 중 p차례에 올 n진법 자릿수를 연결한 t길이의 문자열
    args
        n(int): 2 <= n <= 16, n진법
        t(int): 0 <= t <= 1000, 말해야할 숫자횟수
        m(int): 2 <= m <= 100, 참가인원
        p(int): 1 <= p <= m, 순번
    return  
        (str): t를 구한 문자열
    '''
    res = [""]*(t+1)
    cur, idx, p = 0, 0, p-1
    
    while True:
        for num in int2base(cur, n):
            if idx%m == p:
                res[t] = num
                t -= 1
                if t < 1:
                    return "".join(res[::-1])
            idx += 1
        cur += 1