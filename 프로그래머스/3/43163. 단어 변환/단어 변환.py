from collections import deque

def _word_diff_1(word1: str, word2: str) -> bool:
    return 1 == sum(x != y for x, y in zip(word1, word2))

def solution(begin, target, words):
    try:
        visit = deque([(words.index(target), 1)])
        visited = [True] * len(words)
    except:return 0
    
    while visit:
        cur, cnt = visit.popleft()
        if _word_diff_1(begin, words[cur]):
            return cnt
        
        visited[cur] = False
        for ni, word in enumerate(words):
            if visited[ni] and _word_diff_1(word, words[cur]):
                visited[ni] = False
                visit.append((ni, cnt+1))
    
    return 0