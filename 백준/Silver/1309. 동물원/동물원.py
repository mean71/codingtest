# 동물원 # https://www.acmicpc.net/problem/1309 s1
a,b = 1,2
for _ in range(int(input())):
    a,b = a+b, 2*a + b
print(a%9901)