def solution(n:int, stations:list, w:int) -> int:
    ''' 
    args
        n (int): 아파트개수, 1 <= n <= 2 * 10^8
        stations (list[int]): 기지국이 설치된 위치, 1 <= len <= 1000, 1<= list[i] <= n
        w (int): 전파의 도달거리, 1 <= w <= 10000
    return (int): 모든 아파트에 전파를 전달하기 위한 최소 기지국 증설값
    '''
    idx = 0
    cnt = 0
    width = 2*w+1
    stations.append(n+w+1)
    
    for i in stations:
        cnt += (i + w - idx - 1)//width
        idx = i + w
    diff = n - idx
    
    return cnt