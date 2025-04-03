n = int(input())
i = 2
lst = []

while i*i <= n:
    while n%i == 0:
        lst.append(i)
        n //= i
    i += 1

if n > 1:
    lst.append(n)
    
print(len(lst))
print(*lst)