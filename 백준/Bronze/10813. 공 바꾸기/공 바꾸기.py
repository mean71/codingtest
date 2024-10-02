import sys

read = sys.stdin.readline
N, M = map(int, read().strip().split())
basket = [n+1 for n in range(N)]

for _ in range(M):
  i, j = map(int, read().strip().split())
  i, j = i-1, j-1
  basket[i], basket[j] = basket[j], basket[i]
print(*basket)