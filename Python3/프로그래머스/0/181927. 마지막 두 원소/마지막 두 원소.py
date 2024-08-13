# def solution(nlst):
#     if nlst[-2] < nlst[-1]: nlst.append(nlst[-1] - nlst[-2])
#     else: nlst.append(nlst[-1] * 2)
#     return nlst

# def solution(l):
#     l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
#     return l

solution = lambda l: l + [l[-1] - l[-2] if l[-1] > l[-2] else l[-1] * 2]