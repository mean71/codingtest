import math
import sys
from functools import reduce
input = sys.stdin.readline

N, S = map(int, input().split())
unit = list(map(lambda n: int(n) - S, input().split()))
print(reduce(math.gcd, unit))