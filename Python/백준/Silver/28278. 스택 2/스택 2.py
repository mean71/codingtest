import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    def one(self, elem):
        self.stack.append(elem)

    def two(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def three(self):
        return len(self.stack)
    
    def four(self):
        return 1 if not self.stack else 0
    
    def five(self):
        if not self.stack:
            return -1
        return self.stack[-1]

N = int(input())
stack = Stack()

for _ in range(N):
    n = list(map(int, input().split()))
    if n[0] == 1:
        stack.one(n[1])
    elif n[0] == 2:
        print(stack.two())
    elif n[0] == 3:
        print(stack.three())
    elif n[0] == 4:
        print(stack.four())
    elif n[0] == 5:
        print(stack.five())