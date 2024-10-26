import sys
input = sys.stdin.readline

N,M = map(int, input().split())
nums = list(map(int, input().split()))
# 누적합 리스트
nsum = [0]
for i in nums:
    nsum.append(nsum[-1]+i)

for _ in range(M):
    i,j = map(int, input().split())
    print(nsum[j]-nsum[i-1])