import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
fruits = list(map(int, sys.stdin.readline().split()))

l = 0
max_len = 0
cnt = defaultdict(int)
fruit = 0

for r in range(n):
    cnt[fruits[r]] += 1
    if cnt[fruits[r]] == 1:
        fruit += 1

    while fruit > 2:
        cnt[fruits[l]] -= 1
        if cnt[fruits[l]] == 0:
            fruit -= 1
        l += 1

    max_len = max(max_len, r - l + 1)

print(max_len)