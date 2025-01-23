import sys
input = sys.stdin.readline
res = stack = 0

for c in input(): 
    if c == ")":
        res += not bool(stack)
        stack -= bool(stack)
    elif c == "(":
        stack += 1
print(res + stack)