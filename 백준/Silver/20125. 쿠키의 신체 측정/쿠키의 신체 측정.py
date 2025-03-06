import sys
input = sys.stdin.readline

board = [input() for _ in range(int(input()))]

for i, r in enumerate(board):
    for j, c in enumerate(r):
        if c == "*":
            heart = (i+2, j+1)
            break
    else:
        continue
    break

arm1 = j - board[i+1].find("*")
arm2 = board[i+1].rfind("*") - j
waist = 1

while board[i+3][j] == "*":
    i += 1
    waist += 1

leg1 = i
leg2 = i

for r in range(i+3, len(board)):
    if board[r][j-1] == "*":
        leg1 = r + 1 - heart[0] - waist
    if board[r][j+1] == "*":
        leg2 = r + 1 - heart[0] - waist

print(*heart)
print(arm1, arm2, waist, leg1, leg2)