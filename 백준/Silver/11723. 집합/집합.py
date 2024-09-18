import sys
class Setting():
    def __init__(self):
        self.S = set()
        
    def add(self, x):
        x=int(x)
        self.S.add(x)
    def remove(self, x):
        x=int(x)
        self.S.discard(x)
    def check(self, x):
        x=int(x)
        print(int(x in self.S))
    def toggle(self, x):
        x=int(x)
        if x in self.S:
            self.S.discard(x) == -1
        else:
            self.S.add(x)
    def all(self):
        self.S.clear()
        self.S = {i for i in range(1,21)}
    def empty(self):
        self.S.clear()

M = int(sys.stdin.readline())
setting = Setting()

for _ in range(M):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "add":
        setting.add(cmd[1])
        # print(cmd ,setting.S)
    elif cmd[0] == "remove":
        setting.remove(cmd[1])
        # print(cmd ,setting.S)
    elif cmd[0] == "check":
        setting.check(cmd[1])
        # print(cmd ,setting.S)
    elif cmd[0] == "toggle":
        setting.toggle(cmd[1])
        # print(cmd ,setting.S)
    elif cmd[0] == "all":
        setting.all()
        # print(cmd ,setting.S)
    elif cmd[0] == "empty":
        setting.empty()
        # print(cmd ,setting.S)
    else:
        print("올바르지 않은 주문")