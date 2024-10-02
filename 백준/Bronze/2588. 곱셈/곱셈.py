a=int(input())
b=int(input())

b1,b10,b100 = b % 10, b//10 % 10, b//100
c=b1*a
d=b10*a
e=b100*a

print(c)
print(d)
print(e)
print(c+d*10+e*100)