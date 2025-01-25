sum_AB = []
while True:
  try:
    A,B = map(int, input().strip().split())
    if 0<A<10 and 0<B<10:
      sum_AB.append(A+B)
  except: break
  
for i in sum_AB:
  print(i)