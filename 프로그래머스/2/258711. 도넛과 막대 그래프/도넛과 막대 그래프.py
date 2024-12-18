def solution(edges):
    root = donut = stick = eight = 0
    graph = {}
    parents = {}
    visited = set()
    
    for parent, child in edges:
        graph.setdefault(parent, []).append(child)
        parents[child] =  parents.get(child, 0) + 1
    
    for node, child in graph.items():
        if len(child) > 1 and parents.setdefault(node, 0) == 0:
            root = node
            break
    
    for g in graph[root]:
        cur_child = graph.get(g, [])
        visited.add(g)
        
        while cur_child:
            if len(cur_child) > 1:
                eight += 1
                break
            elif cur_child[0] in visited:
                donut += 1
                break
            visited.add(cur_child[0])
            cur_child = graph.get(cur_child[0], [])
        else:
            stick += 1
            
    return root, donut, stick, eight