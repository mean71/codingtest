def solution(a, b):
    answer = ''
    if all(1 <= x < 10000 for x in [a,b]):
        if int(str(a)+str(b)) >= int(str(b)+str(a)):
            answer=int(str(a)+str(b))
        else:
            answer=int(str(b)+str(a))
        return answer