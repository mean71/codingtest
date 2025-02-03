dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for t in range(1, int(input()) + 1):
    N,M = map(int, input().split())
    balloons = [[0]*(M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(M + 2)]
    max_cnt = 0
    
    for r in range(1, N+1):
        for c in range(1, M+1):
            cnt = balloons[r][c]
            for i in range(4):
                cnt += balloons[r+dr[i]][c+dc[i]]
            max_cnt = max(max_cnt, cnt)
    
    print(f'#{t} {max_cnt}')