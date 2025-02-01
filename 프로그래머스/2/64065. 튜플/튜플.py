# 튜플
from collections import Counter

def solution(s):
    return [int(n) for n, _ in Counter("".join(c if c.isdigit() else " " for c in s).split()).most_common()]