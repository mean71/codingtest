import sys
input = sys.stdin.readline

N, M, V = map(int, input().split()) # 노드개수n , 질문 횟수, 끝 노드에 연결된 노드번호
lst = list(map(int, input().split())) # i번째는 i번 노드에 저장된 값

for _ in range(M):
    k = int(input())
    
    if k < V - 1:
        print(lst[k])
    else:
        print(lst[(k-V+1)%(N-V+1) + V - 1])