from itertools import permutations

def permutations(arr, k):
    if k == 0:
        yield []
    for i, fi in enumerate(arr):
        for next in permutations(arr[:i] + arr[i+1:], k-1):
            yield [fi] + next

N, M = map(int, input().split())
arr = [str(i) for i in range(1, N+1)]

for s in permutations(arr, M):
    print(" ".join(s))