def solution(a, d, included):
    adsum = 0
    if 1<=a<=100 and 1<=d<=100 and 1<=len(included)<=100 and 1<=included.count(True):
        for i,j in enumerate(included):
            sumad=a+d*i
            if j == True:
                adsum+=sumad
    return adsum