from collections import deque

def solution(cacheSize, cities):
    if not cacheSize: return len(cities)*5
    cache_set = set()
    cache_que = deque(maxlen=cacheSize)
    res = 0
    
    
    for city in cities:
        city = city.lower()
        if city in cache_set:
            res += 1
            cache_que.remove(city)
            cache_que.append(city)
        else:
            res += 5
            cache_set.add(city)
            if len(cache_set) > cacheSize:
                cache_set.discard(cache_que.popleft())
            cache_que.append(city)

    return res