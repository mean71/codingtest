def solution(nlst):
    if nlst[-2] < nlst[-1]: nlst.append(nlst[-1] - nlst[-2])
    else: nlst.append(nlst[-1] * 2)
    return nlst