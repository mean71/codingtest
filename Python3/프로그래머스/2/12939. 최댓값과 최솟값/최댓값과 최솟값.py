def solution(s):
    s = list(map(int,(s.strip().split(' '))))
    answer = f'{min(s)} {max(s)}'
    return answer