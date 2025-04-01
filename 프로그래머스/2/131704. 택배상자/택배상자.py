def solution(order) -> int: # 1 <= len(order) <= 10^6
    stack = []
    i = 0
    for n in range(1, len(order)+1):
        stack.append(n)
        while stack and stack[-1]==order[i]:
            stack.pop()
            i += 1
    
    return i