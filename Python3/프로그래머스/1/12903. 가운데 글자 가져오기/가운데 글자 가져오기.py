solution = lambda s: (lambda l: s[l] if len(s)%2 else s[l-1:l+1])(len(s)//2)
