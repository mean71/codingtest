def solution(a, b):
    if all(1 <= x < 10000 for x in (a,b)):
        answer=max(f'{a}{b}',f'{b}{a}')
        return int(answer)