import sys
input = sys.stdin.readline

N,K = map(int,input().split())
temps = list(map(int, input().split()))
#초기값 설정
max_temp = sum_temp = sum(temps[:K])
l,r = 0,K
# 슬라이딩 윈도우
for i in range(N-K):
    if max_temp < (sum_temp := sum_temp + temps[i+K] - temps[i]):
        max_temp = sum_temp
print(max_temp)