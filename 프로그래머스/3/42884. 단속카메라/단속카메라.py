import heapq

def solution(routes:list) -> int:
    '''
    args
        routes (list[list[int]]): [[in_distance, out_distance]]
    return (int): 모든 차량을 단속가능한 최소 단속카메라 갯수
    '''
    routes.sort(key=lambda x:x[1])
    cctv_latedist = -30001
    cnt = 0
    
    for i,o in routes:
        if i > cctv_latedist:
            cnt += 1
            cctv_latedist = o
    
    return cnt

#     heapq.heapify(routes)
#     inplace = []
#     cnt = 0
    
#     for i in range(len(routes)):
#         in_dist, out_dist = heapq.heappop(routes)
        
#         if inplace and in_dist >= inplace[0][0]:
#             cnt += 1
        
#         while inplace and in_dist >= inplace[0][0]:
#             heapq.heappop(inplace)
        
#         heapq.heappush(inplace, (out_dist, in_dist))
    
#     return cnt