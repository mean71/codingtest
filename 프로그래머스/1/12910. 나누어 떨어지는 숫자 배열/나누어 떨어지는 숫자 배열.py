solution = lambda a,d: (lambda x: x if x else [-1])(sorted(e for e in a if not e%d))
    