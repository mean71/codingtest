N ,X= map(int,input().strip().split())
A = list(map(int,input().strip().split()))
def test(x):
  return 1<= x <= 10000
def Xsize(x,y):
  if x > y: return y
def sx(n,x,a):
  prx = []
  if test(n) and test(x):
    for i in range(len(a)):
      if Xsize(x,a[i]):
        prx.append(a[i])
  return prx

print(*sx(N,X,A))