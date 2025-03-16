from itertools import combinations

def combinations(arr, k):
    if k == 0:
        yield []
    for i, fi in enumerate(arr):
        for next in combinations(arr[i+1:], k-1):
            yield [fi] + next
        
N, M = map(int, input().split())
arr = list(range(1, N+1))

for s in combinations(arr, M):
    print(*s)