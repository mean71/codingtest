def solution(s):
    s = list(map(int,(s.strip().split(' '))))
    return f'{min(s)} {max(s)}'