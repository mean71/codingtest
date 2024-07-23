def solution(a, b):
    answer = 0
    if all(1<=x<=10000 for x in[a,b]):
        answer=max(int(f'{a}{b}'),2*a*b)
    return answer