import sys
input = sys.stdin.readline

N, A, D = map(int, input().split())
sound = list(map(int, input().split()))
cnt = 0

for n in sound:
    if A == n:
        A += D
        cnt += 1

print(cnt)