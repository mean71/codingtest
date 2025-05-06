import sys
input = sys.stdin.readline

n = int(input())
adj_lst = [[1 if (i=="Y") else float("inf") for i in input().rstrip()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            adj_lst[j][k] = min(adj_lst[j][k], adj_lst[j][i] + adj_lst[i][k])

for i in range(n):
    adj_lst[i][i] = float("inf")

print(max(sum(j <= 2 for j in i) for i in adj_lst))