import heapq

def solution(n: int, works: list) -> int:
    '''1작업/1시간 처리가능, 야근 피로도는 야근 시작시점에 남은일의 작업량을 제곱하여 더한값
    args
        n(int): 퇴근까지 남은시간
        works(list[int]): 각 일에 대한 작업량
    return (int): 야근피로도를 최소화한 결과값
    '''
    if sum(works) < n:
        return 0
    
    works = [-i for i in works]
    heapq.heapify(works)
    
    for _ in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1)
    
    return sum(i**2 for i in works)