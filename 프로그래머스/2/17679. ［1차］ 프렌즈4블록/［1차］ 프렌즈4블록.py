def _check_block(n, m, board):
    cr = set()
    for i in range(n - 1):
        for j in range(m - 1):

                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != False:
                    cr.update([(i,j), (i+1,j), (i,j+1), (i+1,j+1)])
    return cr
    
def _drop_block(n, m, board, crush):
    for i, j in crush:
        board[i][j] = False
    for j in range(m):
        temp = [board[i][j] for i in range(n) if board[i][j]]
        for i in range(n - 1, -1, -1):
            board[i][j] = temp.pop() if temp else False
    return board

def solution(m, n, board):
    '''
    args
        n(int), m(int): board height & width, 2 <= (n, m) <= 30
        board: (n * m) [A-Z]+ block map
    return int
    '''
    board = [list(r) for r in board]
    check = True
    cnt = 0
    
    while (crush := _check_block(m, n, board)):
        board = _drop_block(m, n, board, crush) 
        cnt += len(crush)
    
    return cnt

if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  #  14
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) #  15