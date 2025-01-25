T = int(input())
a = []
for i in range(T):
    A,B=map(int, input().strip().split())
    a.append(A+B)
for i in range(T):
    print(f'Case #{i+1}: {a[i]}')