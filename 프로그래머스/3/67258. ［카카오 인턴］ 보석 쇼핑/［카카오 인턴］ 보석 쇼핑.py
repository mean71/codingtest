from collections import defaultdict
from typing import List

def solution(gems: List[str]) -> List[int]:
    """
    입력: 문자열 리스트 gems
    조건: 모든 종류의 보석을 구매하는 최소구간
    출력: 조건을 만족하는 인덱스 [s, e]
    """
    size = len(set(gems))
    res = [0, len(gems) - 1]
    l, r = 0, 0
    gem_info = defaultdict(int)
    gem_info[gems[0]] += 1  

    while r < len(gems):
        if len(gem_info) == size:
            if r - l < res[1] - res[0]:
                res = [l, r]
            gem_info[gems[l]] -= 1
            if gem_info[gems[l]] == 0:
                del gem_info[gems[l]]
            l += 1
        else:
            r += 1
            if r == len(gems):
                break
            gem_info[gems[r]] += 1

    return [res[0] + 1, res[1] + 1]