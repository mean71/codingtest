student_num = [_ for _ in range(1,31)]
n=[]
for i in range(28):
  n.append(int(input()))
for i in student_num:
  if i not in n:
    print(i)