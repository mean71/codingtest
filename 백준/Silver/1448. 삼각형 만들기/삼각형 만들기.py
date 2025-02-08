import sys
input = sys.stdin.readline

n = int(input())
line = sorted((int(input()) for _ in range(n)), reverse=True)

for n in range(n-2):
    if line[n] < line[n+1] + line[n+2]:
        print(sum(line[i] for i in range(n, n+3)))
        break
else:
    print(-1)