N = int(input())
n = list(map(int, input().strip().split()))
v = int(input())

result = 0
for x in range(N):
  if v == n[x]:
    result += 1
print(result)