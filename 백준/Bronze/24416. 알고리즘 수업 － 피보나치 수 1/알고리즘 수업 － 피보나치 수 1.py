n = int(input())
a,b = 1,1
for _ in range(1, n):
    a,b = b, a+b
print(a, max(1, n-2))