import sys
input = sys.stdin.readline

inside = set()
error_cnt = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b:
        if a in inside:
            error_cnt += 1
            continue
        inside.add(a)
    else:
        if a not in inside:
            error_cnt += 1
            continue
        inside.discard(a)

print(error_cnt+len(inside))