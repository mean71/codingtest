for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            bugs = sum(arr[i][j] for i in range(r, r+M) for j in range(c, c+M))
            res = max(res, bugs)
    print(f"#{t} {res}")