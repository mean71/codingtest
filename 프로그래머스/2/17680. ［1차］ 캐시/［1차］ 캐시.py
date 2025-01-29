from collections import deque

def solution(cacheSize, cities):
    cache_que = deque(maxlen=cacheSize)
    res = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache_que:
            res += 1
            cache_que.remove(city)
            cache_que.append(city)
        else:
            res += 5
            cache_que.append(city)
        
    return res