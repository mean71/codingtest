import sys
input = sys.stdin.readline
n = int(input())
vote = sorted(int(input()) for _ in range(n))
drop = int(n*0.15 + 0.5)
if not n or n - 2*drop <= 0:
    print(0)
else:
    print(int(sum(vote[drop:n-drop]) / (n - 2*drop) + 0.5))