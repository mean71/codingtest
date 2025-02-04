def solution(citations):
    return next(i for i,n in enumerate(sorted(citations+[0], reverse=True)) if i >= n )
x = map(int, input().split())

print(solution(list(x)))