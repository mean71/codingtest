N = int(input())
Numpy = list(map(int, input().strip().split()))
def condition(i):
  if 1 <= i <= 1000000:
    return True
def minmax(Numpy):
  return f'{min(Numpy)} {max(Numpy)}'

print(minmax(Numpy))