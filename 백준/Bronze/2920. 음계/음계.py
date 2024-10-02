N = list(map(int, input().split()))
if N == sorted(N):print('ascending')
elif N == sorted(N)[::-1]:print('descending')
else:print('mixed')