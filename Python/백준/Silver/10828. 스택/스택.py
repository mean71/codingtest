import sys

N = int(sys.stdin.readline())
stack_lst = []
def stack(command):
    if command[0] == 'pop':
        print(stack_lst.pop() if stack_lst else -1)
    elif command[0] == 'size':
        print(len(stack_lst))
    elif command[0] == 'empty':
        print(0 if stack_lst else 1)
    elif command[0] == 'top':
        print(stack_lst[-1] if stack_lst else -1)
    else:
        stack_lst.append(command[-1])

for i in range(N):
    command = sys.stdin.readline().strip().split()
    stack(command)