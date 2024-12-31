# 아이템 줍기 # bfs # 미해결
from collections import deque
from typing import List

def solution(rectangles: List[List[int]], cX:int, cY:int, itemX:int, itemY:int) -> int:
    """아이템을 줍기 위한 최소 이동거리
    args:
        rectangles (List[List[int]]): 금지된 좌표
        cX (int): 캐릭터 x좌표
        cY (int): 캐릭터 y좌표
        itemX (int): 아이템 x좌표
        itemY (int): 아이템 y좌표
    return:
        int: 최소 이동거리
    """
    edge = set()
    rectangles = [list(map(lambda x:2*x, i)) for i in rectangles]
    # edge
    for rect in rectangles:
        #가로줄 추가 y는(rect[1,3으로 고정])
        for x in range(rect[0], rect[2] + 1):
            edge.add((x, rect[1]))
            edge.add((x, rect[3]))
        #세로줄 추가
        for y in range(rect[1], rect[3] + 1):
            edge.add((rect[0], y))
            edge.add((rect[2], y))
    # inline 제거
    for rect in rectangles:
        for x in range(rect[0] + 1, rect[2]):
            for y in range(rect[1] + 1, rect[3]):
                edge.discard((x,y))
    # 시각화
    # for i in range(20,-1,-1):
    #     print("".join("- " if (j,i) not in edge else "+ " for j in range(21)))
    # (cX, cY) -> (itemX, itemY)
    # 매번 현재위치가 target인지 검사
    # 상하좌우좌표 in edge 경로가 있는지 검사
    # 경로가 있다면 탐색한 경로를 제거한 뒤 해당 방향으로 좌표 한칸 더 옮기고 이동 횟수 1추가 -> 큐.apennd()
    queue = deque([(cX*2, cY*2, 0)])
    target = (itemX*2, itemY*2)
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    while queue:
        x, y, cnt = queue.popleft()
        cur = x, y
        
        if cur == target:
            return cnt
        for i in range(4):
            nx, ny = cur[0]+dx[i], cur[1]+dy[i]
            if (nx, ny) in edge:
                edge.discard((nx, ny))
                queue.append((nx+dx[i], ny+dy[i], cnt+1))
    
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))