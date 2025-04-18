# import sys
# input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())
kcal = sorted((int(input()) for _ in range(N)), reverse=True)
total_kcal = C
total_price = A
max_kcal = C//A

for i in range(N):
    total_price += B
    total_kcal += kcal[i]
    cost_k = total_kcal//total_price
    if max_kcal < cost_k:
        max_kcal = cost_k
    else:
        break

print(max_kcal)