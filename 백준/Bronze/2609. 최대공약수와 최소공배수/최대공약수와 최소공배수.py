A,B = map(int, input().split())
a,b = A,B
while b:
    a,b = b, a%b
x = a
y = A*B//a
print(x)
print(y)