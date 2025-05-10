import sys
sys.setrecursionlimit(10**6)

def solution(arr):
    ans = [0, 0]
    
    def _divid(x, y, size):
        num = arr[x][y]
        if all(arr[i][j]==num for i in range(x, x+size) for j in range(y, y+size)):
            ans[num] += 1
            return
        
        mid = size//2
        for dx, dy in ((0,0), (0,mid), (mid,0), (mid,mid)):
            _divid(x+dx, y+dy, mid)
    
    _divid(0, 0, len(arr))
    return ans