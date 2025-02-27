from itertools import product
import sys

def dfs(cur, word, visit=None, cnt=None):
    if cnt is None:
        visit = []
        cnt = [0]
    
    if len(cur) < 5:
        for c in "UOIEA":
            visit.append(cur + c)
    
    if cur != word:
        cnt[0] += 1
    else:
        return cnt[0]
    
    if visit:
        return dfs(visit.pop(), word, visit, cnt)
    
def solution(word):
    sys.setrecursionlimit(100000)
    return dfs("", word)