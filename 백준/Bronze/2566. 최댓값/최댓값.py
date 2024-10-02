import sys
a = [sys.stdin.readline().strip('\n').split() for _ in range(9)]
b=''
for i in range(9):
    for j in range(9):
        if len(b)<len(a[i][j]) or b < a[i][j]:
            b = a[i][j]
            res = [i+1, j+1]

print(f'{b}\n{res[0]} {res[1]}')