def solution(mats, park):
    mats.sort()
    min_mat = mats[0]
    res = -1
    for r in range(len(park) + 1 - min_mat):
        for c in range(len(park[0]) + 1 - min_mat):
            for i,mat in enumerate(mats[::-1]):
                if len(park) > r+mat-1 and len(park[0]) > c+mat-1:
                    for dr in range(mat):
                        if any(x!="-1" for x in park[r+dr][c:c+mat]):
                            break
                    else:
                        res = mat
                        del mats[:len(mats)-i]
                        if not mats:
                            return res
                        break
                
    return res
                        
                        