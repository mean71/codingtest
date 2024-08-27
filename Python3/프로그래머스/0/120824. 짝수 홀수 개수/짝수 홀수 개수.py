# solution = lambda n: [ len([i for i in n if not i%2]), len([i for i in n if i%2]) ]
# solution = lambda n: [ sum(i%2 == 0 for i in n), sum(i%2 != 0 for i in n) ]
solution = lambda n: [sum([not(n%2) for n in n]), sum([n%2 for n in n])]