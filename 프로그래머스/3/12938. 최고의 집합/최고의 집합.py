def solution(n:int, s:int) -> list:
    div, n_mod_diff = s//n, n-s%n
    return [-1] if s < n else [div + (i >= n_mod_diff) for i in range(n)]