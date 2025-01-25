import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    
    # 두 원의 중심 사이의 거리
    x_y = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    r_sum = r1 + r2
    r_diff = abs(r1 - r2)

    if x_y > r_sum:
        print(0)  # 멀때
    elif x_y == 0:
        if r1 == r2:
            print(-1)  # 두 원이 완전히 일치함
        else:
            print(0)
    elif x_y == r_sum:
        print(1)  # 외접
    elif x_y == r_diff:
        print(1)  # 내접
    elif x_y < r_diff:
        print(0)
    else:
        print(2)
    