# def solution(n):
#     a=0
#     for i in range(n):
#         if n%(i+1) == 0:
#             a += i+1
#     return

def solution(n):
    if n==0: return 0
    elif n==1: return 1
    else: return sum([i+1 for i in range(1,n//2+1) if not n%(i+1)])+n+1