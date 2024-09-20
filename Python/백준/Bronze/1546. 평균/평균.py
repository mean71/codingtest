N = int(input())
score = list(map(int,input().strip().split()))
def a(N,score):
  avg=[]
  if N <= 1000:
    M = max(score)
    for i in range(len(score)):
      avg.append(score[i]/M*100)
  return sum(avg)/len(avg)
print(a(N,score))