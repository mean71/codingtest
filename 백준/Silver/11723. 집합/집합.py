import sys
input = sys.stdin.readline
s = 0
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "add":
        s |= 1 << int(cmd[1])-1
    elif cmd[0] == "remove":
        s &= ~(1 << int(cmd[1])-1)
    elif cmd[0] == "check":
        print((s >> int(cmd[1])-1) & 1)
    elif cmd[0] == "toggle":
        s ^= 1 << int(cmd[1])-1
    elif cmd[0] == "all":
        s = (1 << 20) - 1
    elif cmd[0] == "empty":
        s = 0
    else:
        print("올바르지 않은 주문")