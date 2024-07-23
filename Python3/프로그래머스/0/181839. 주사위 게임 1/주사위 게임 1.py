def solution(a, b):
    answer = 0
    if 1<=a<=6 and 1<=b<=6:
        if (a+b)%2==0:
            if a%2!=0:
                answer = a**2 + b**2
            else:
                answer = abs(a-b)
        else:
            answer = 2*(a+b)
    return answer