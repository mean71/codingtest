import sys
from itertools import permutations
input = sys.stdin.readline

N, K = int(input()), int(input()) # 4<=n<=10, 2<=k<=4
cards = [input().strip() for _ in range(N)]
num_set = set()

for s in permutations(cards, K):
    num_set.add("".join(s))

print(len(num_set))