T = int(input())
str = ''
for _ in range(T):
  R, S = input().split()
  R = int(R)
  for i in S:
    str += i*R
  str += '\n'
print(str)