x = int(input())
n = 1

while x > n:
    x -= n
    n += 1
if n%2:
    X = n-x+1, x
else:
    X = x, n-x+1

print(f'{X[0]}/{X[1]}')