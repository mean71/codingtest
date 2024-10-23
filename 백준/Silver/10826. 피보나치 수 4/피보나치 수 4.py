
import sys
input = sys.stdin.readline

def fibonacci(num):
    a,b = 1, 0
    for _ in range(num):
        a,b = b, a+b
    return b
print(fibonacci(int(input())))