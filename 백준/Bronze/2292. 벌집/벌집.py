n = int(input())
res = 0
min_floor = 1
while 1:
    max_floor = min_floor + res*6
    if min_floor <= n <= max_floor:
        res += 1
        break
    min_floor = max_floor
    res += 1
print(res)