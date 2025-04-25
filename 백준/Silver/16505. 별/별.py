n = int(input())
s = ["*"]

for i in range(n):
    s.extend([r.ljust(2**i, " ") + r for r in s])

print(*s[::-1], sep="\n")