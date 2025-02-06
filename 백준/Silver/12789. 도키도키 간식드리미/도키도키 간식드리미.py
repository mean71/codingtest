import sys
input = sys.stdin.readline
N = int(input())
line = list(map(int, input().split()))
stack = []
idx = 0

for n in range(1, N + 1):
    # 현재 스택의 top이 n이면 pop
    if stack and stack[-1] == n:
        stack.pop()
        continue
    
    # line에서 n을 찾을 때까지 stack에 넣기
    while idx < N and line[idx] != n:
        stack.append(line[idx])
        idx += 1

    # n을 찾았다면 바로 pop하고 다음 수로
    if idx < N and line[idx] == n:
        idx += 1
    else:
        print("Sad")
        break
else:
    print("Nice")
