def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif i != stack[-1]:
            stack.append(i)
        else:
            stack.pop(-1)
    return int(not stack)