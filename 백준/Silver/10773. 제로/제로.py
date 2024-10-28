import sys
input = sys.stdin.readline

import collections as cl
stack = cl.deque()
for _ in range(int(input())):
    if n:=int(input()):
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))