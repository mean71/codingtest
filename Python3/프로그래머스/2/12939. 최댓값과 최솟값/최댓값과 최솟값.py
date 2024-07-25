def solution(s):
    str = list(map(int,(s.strip().split(' '))))
    answer = f'{min(str)} {max(str)}'
    return answer