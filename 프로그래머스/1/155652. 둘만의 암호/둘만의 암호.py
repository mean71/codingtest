def solution(s, p, i):
    alpha = [c for c in "abcdefghijklmnopqrstuvwxyz"if c not in p]
    return "".join(alpha[(alpha.index(c) + i) %len(alpha)] for c in s)