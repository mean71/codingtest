N, M = map(int, input().split())
res = {input() for _ in range(N)} & {input() for _ in range(M)}
print(len(res))
[print(s) for s in sorted(res)]