import sys
input = sys.stdin.readline
stack = [-1]

for c in input():
    if c == ")":
        if stack[-1] == "(":
            stack.pop()
            continue
        stack[0] += 1
    elif c == "(":
        stack.append(c)
        
print(stack[0] + len(stack))