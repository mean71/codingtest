import sys
input = sys.stdin.readline

class Setting():
    def __init__(self):
        self.S = 0
    
    def __call__(self, cmd):
        if cmd[0] == "add":
            self.add(cmd[1])
        elif cmd[0] == "remove":
            self.remove(cmd[1])
        elif cmd[0] == "check":
            self.check(cmd[1])
        elif cmd[0] == "toggle":
            self.toggle(cmd[1])
        elif cmd[0] == "all":
            self.all()
        elif cmd[0] == "empty":
            self.empty()
        else:
            print("올바르지 않은 주문")
    
    def add(self, x):
        self.S |= 1 << int(x)-1
    def remove(self, x):
        self.S &= ~(1 << int(x)-1)
    def check(self, x):
        print((self.S >> int(x)-1) & 1)
    def toggle(self, x): # S.remove(x) if (x in S) else S.add(x)
        self.S ^= 1 << int(x)-1
    def all(self): # range(1,21)
        self.S = (1 << 20) - 1
    def empty(self): # 공집합
        self.S = 0

S = Setting()

for _ in range(int(input())):
    cmd = input().split()
    S(cmd)