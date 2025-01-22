def solution(id_list, report, k):
    id_list = {key: [set(), 0] for key in id_list}
    
    for p1,p2 in map(lambda s:s.split(), report):
        id_list[p2][0].add(p1)
        
    for list_id in id_list.values():
        if len(list_id[0]) >= k:
            for key in list_id[0]:
                id_list[key][1] += 1
                
    return [user[1] for user in id_list.values()]