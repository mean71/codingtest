# s4 4949번 균형잡힌 세상
import sys
input = sys.stdin.readline

brackets = {')': '(', ']': '['}

while (line := input().rstrip()) != '.':
    stack = []
    for char in line:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack.pop() != brackets[char]:
                stack.append(char)
                break
    print('yes' if not stack else 'no')