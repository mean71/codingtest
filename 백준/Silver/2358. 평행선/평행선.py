import sys
from collections import defaultdict
input = sys.stdin.readline

x = defaultdict(int)
y = defaultdict(int)
cnt = 0

for _ in range(int(input())): # 1 <= n <= 10^5
    i, j = map(int, input().split()) # |x|,|y| < 2^31
    x[i] += 1
    y[j] += 1

for i in x.values():
    if i > 1:
        cnt += 1

for i in y.values():
    if i > 1:
        cnt += 1

print(cnt)