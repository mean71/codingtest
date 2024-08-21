import sys
read = sys.stdin.readline
# (1 ≤ i ≤ j ≤ N)
N, M = map(int, read().split())
basket = [n+1 for n in range(N)]
for _ in range(M):
  i, j = map(int, read().split())
  for k in range((j - i + 1)//2):
    basket[i+k-1],basket[j-k-1] = basket[j-k-1], basket[i+k-1]
print(*basket) 