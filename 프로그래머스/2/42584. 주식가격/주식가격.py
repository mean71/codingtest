def solution(prices):
    # 2 <= len(prices) <= 10^5, 1 <= prices[i] <= 10^4
    time = [0]*len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            time[j] =  i - j    
        stack.append(i)
    
    while stack:
        j = stack.pop()
        time[j] = i -j
    
    return time 