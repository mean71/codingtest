solution = lambda a,b: sum( i for i in (range(a,b+1) if a<=b else range(b,a+1)) )