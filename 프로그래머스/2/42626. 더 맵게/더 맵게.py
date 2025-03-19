import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    res = 0
    while scoville[0] < K:
        res += 1
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        except:
            return -1
    return res