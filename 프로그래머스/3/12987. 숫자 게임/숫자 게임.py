import heapq

def solution(A:list, B:list) -> int:
    '''그리디
    경기당 양팀에서 한명씩 번호를 비교하여 큰쪽이 승리하고 1점 득점
    B팀이 얻는 최대승점 반환
    args: 출전순으로 번호가 나열된 배열 A와 아닌 배열 B
        A(list[int]): 1 <= len(A)==len(B) <= 10^5
        B(list[int]): 1 <= (A[i] or B[i]) <= 10^9
    return (int): 
    '''
    A = [-i for i in A]
    B = [-i for i in B]
    heapq.heapify(A)
    heapq.heapify(B)
    cnt = 0
    
    while B:
        b = heapq.heappop(B)
        while A:
            if b < heapq.heappop(A):
                cnt += 1
                break
    
    return cnt