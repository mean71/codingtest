import sys
input = sys.stdin.readline

color_dic = {}
total_dist = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    if y in color_dic:
        color_dic[y].append(x)
    else:
        color_dic[y] = [x]

for lst in color_dic.values():
    lst.sort()
    
    if len(lst) == 1:
        continue
    
    for i in range(len(lst)):
        l = lst[i] - lst[i-1] if i > 0 else float("inf")
        r = lst[i+1] - lst[i] if i < len(lst)-1 else float("inf")
        total_dist += min(l, r)

print(total_dist)