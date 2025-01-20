def solution(friends, gifts):
    record = {k: [0, {k:0 for k in friends}, 0] for k in friends}
    
    for a,b in map(lambda x:x.split(), gifts):
        record[a][0] += 1
        record[b][0] -= 1
        record[a][1][b] += 1
        record[b][1][a] -= 1
    
    for fi in range(len(friends)-1):
        f1 = friends[fi]
        for f2 in friends[fi+1:]:
            if record[f1][1][f2] > record[f2][1][f1]:
                record[f1][2] += 1
            elif record[f1][1][f2] < record[f2][1][f1]:
                record[f2][2] += 1
            else:
                if record[f1][0] > record[f2][0]:
                    record[f1][2] += 1
                if record[f1][0] < record[f2][0]:
                    record[f2][2] += 1
    
    return max(record[k][2] for k in friends)