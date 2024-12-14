import sys
input = sys.stdin.readline

adj_lst = [input().split() for _ in range(5)]
dr, dc = (-1,1,0,0), (0,0,-1,1)
nums = set()

def dfs(r, c, num=''):
    if len(num) == 6:
        nums.add(num)
        return
    for i in range(4):
        ri, ci = r + dr[i], c + dc[i]
        if 0 <= ri < 5 and 0 <= ci < 5:
            dfs(ri, ci, num + adj_lst[ri][ci])

for r in range(5):
    for c in range(5):
        dfs(r, c)
print(len(nums))