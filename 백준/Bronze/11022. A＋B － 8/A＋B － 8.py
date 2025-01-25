T = int(input())
sum_ab=[]
A_B=[]
for t in range(T):
    A,B = map(int, input().strip().split())
    A_B.append((A, B))
    sum_ab.append(A + B)
for t in range(T):
    print(f'Case #{t+1}: {A_B[t][0]} + {A_B[t][1]} = {sum_ab[t]}')