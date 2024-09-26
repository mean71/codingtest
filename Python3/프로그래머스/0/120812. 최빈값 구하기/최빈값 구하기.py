def solution(x):
    dic = {}
    kc = 0
    mode = 0
    
    for i in x:
        if i in dic: dic[i] += 1
        else: dic[i] = 1

    for key,count in dic.items():
        if kc == 0: kc, mode = count, key
        elif kc < count: kc, mode = count ,key
        elif kc == count: mode = -1
    return mode