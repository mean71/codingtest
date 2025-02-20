N = int(input())
a,b = 1,1
for _ in range(N):
    a,b = b, a+b
print(a)