import sys
import heapq
input = sys.stdin.readline

N, X = map(int, input().split())
max_A = (X - 1000*N)//4000
total = 0
l_A = []
heapq.heapify(l_A)


for _ in range(N):
    A, B = map(int, input().split())
    total += B
    if A > B:
        heapq.heappush(l_A, B - A)

if len(l_A) <= max_A:
    total -= sum(l_A)
else:
    for _ in range(max_A):
        total -= heapq.heappop(l_A)

print(total)