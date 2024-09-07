import sys

credits = [sys.stdin.readline().split() for _ in range(20)]
subjects = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
         'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
lst=[[],[]]

for c in credits:
    if c[2] != 'P':
        lst[1].append(float(c[1])*subjects[c[2]])
        lst[0].append(float(c[1]))
print(f'{sum(lst[1])/sum(lst[0]):.6f}')