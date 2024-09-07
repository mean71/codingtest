# solution = lambda a,b: [[sum(e) for e in zip(i,j)] for i,j in zip(a,b)]
solution = lambda a,b: [list(map(sum, zip(*i))) for i in zip(a,b)]