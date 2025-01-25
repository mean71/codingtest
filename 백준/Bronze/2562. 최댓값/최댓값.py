import sys
n = []
for i in range(9):
  n.append( int(sys.stdin.readline().strip()) )
print( f'{max(n)}\n{n.index(max(n))+1}' )