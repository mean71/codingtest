import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split()) # 방의 크기 3 <= N,M <= 50
r,c,d = map(int, input().split()) # 현재좌표(r,c) 방향d = 0/1/2/3  = 북/동/남/서
rooms = [list(map(int, input().split())) for _ in range(N)] # N*M 방의 상태를 나타내는 값
dr, dc = (-1,0,1,0), (0,1,0,-1) # 진행좌표 인덱스 d에 따른 좌표이동 정의
cleaning = 0 # 청소횟수

while (room:=rooms[r][c])!=1: # 조회할 이동 좌표가 벽이면 정지
    if not rooms[r][c]: # 청소상태검사 -> 변경 -> 횟수카운트
        rooms[r][c] = 2
        cleaning +=1
    # 4방향 확인
    for x in range(d+7, d+3, -1): # 현재 좌표 주변 4칸을 # 반시계방향으로 조회하며 방향대입
        d = x%4
        nr,nc = r + dr[d], c + dc[d]
        if not rooms[nr][nc]: # 청소가 안된곳이라면
            r,c = nr,nc # 해당좌표로 전진하고 조회정지
            break
    else: # 4방향을 다 돌아봐도 0이 없다면 실행
        if 0 <= (r:= r-dr[d]) < N and 0 <= (c:= c-dc[d]) < M:pass # 후진하고 인덱스 범위검사
print(cleaning)