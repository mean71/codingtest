def solution(record):
    '''
    args record(List[str]):
    return (List[str]):
    '''
    id_name = {}
    res = []
    
    for q in record:
        q = q.split()
        if q[0] == "Enter":
            id_name[q[1]] = q[2]
            res.append((q[1], "님이 들어왔습니다."))
        elif q[0] == "Leave":
            res.append((q[1], "님이 나갔습니다."))
        elif q[0] == "Change":
            id_name[q[1]] = q[2]
    
    return [id_name[_id] + i_o for _id, i_o  in res]