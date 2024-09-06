import sys
w = sys.stdin.readline().split()
crap = ('c=','c-','dz=','d-','lj','nj','s=','z=')

for i in crap:
    if w[0].count(i):
        w[0]=w[0].replace(i,'0')
        
print(len(w[0]))