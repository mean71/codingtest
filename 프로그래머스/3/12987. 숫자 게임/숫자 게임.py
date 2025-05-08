import heapq

def solution(A:list, B:list) -> int:
    '''그리디
    A,B팀의 각 팀원이 무작위번호를 부여받아 한번씩 경기
    각 경기당 각팀에서 한명씩 나와 번호를 비교하여 큰쪽이 승리하고 1점 득점
    같다면 무득점
    A팀은 자신의 출전순서를 B팀에게 공개
    B팀은 그걸 보고 자신들의 최종 승점을 가장 높이는 방법으로 정했다
    이때 B팀이 얻는 최대승점
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