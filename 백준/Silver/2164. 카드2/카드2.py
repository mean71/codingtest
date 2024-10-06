import collections as cl
N = int(input())
card = cl.deque(i for i in range(1,N+1))
for _ in range(N-1):
    card.popleft()
    card.append(card.popleft())
print(card.pop())