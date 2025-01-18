def solution(board, moves):
    board = [[n for n in x if n] for x in zip(*board[-1::-1])]
    stack = [0]
    res = 0
    
    for i in moves:
        if board[i-1]:
            stack.append(board[i-1].pop())
            if stack[-1]==stack[-2]:
                del stack[-2:]
                res += 2
                
    return res