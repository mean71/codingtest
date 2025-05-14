import heapq
import sys
input = sys.stdin.readline

start_heap = []
end_heap = []
room = 0

for _ in range(int(input())):
    n, start, end = map(int, input().split())
    heapq.heappush(start_heap, (start, end))

while start_heap:
    start, end = heapq.heappop(start_heap)
    
    while end_heap and end_heap[0] <= start:
        heapq.heappop(end_heap)
    
    heapq.heappush(end_heap, end)
    room = max(room, len(end_heap))

print(room)