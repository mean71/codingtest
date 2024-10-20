import sys
input=sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))
x = int(input())
count = 0
num_j = set()
for i in n:
    if x-i in num_j:
        count += 1
    num_j.add(i)
print(count)