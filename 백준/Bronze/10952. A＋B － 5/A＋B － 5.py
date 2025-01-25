sum_AB=[]
while True:
    A,B = map(int, input().strip().split())
    if 0<A<10 and 0<B<10:
      sum_AB.append( sum([A,B]) )
    else: break
for n in range(len(sum_AB)):
    print(sum_AB[n])