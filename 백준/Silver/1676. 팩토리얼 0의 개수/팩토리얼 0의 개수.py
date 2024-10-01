N = int(input())
a,b = 1,0
for n in range(N):
    a*=n+1
while a%10==0:
    b+=1
    a//=10

print(b)