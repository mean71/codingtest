solution = lambda s,n: ''.join([("ABCDEFGHIJKLMNOPQRSTUVWXYZ"["ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(i)+n if 25>"ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(i)+n else "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(i)+n-26] if (i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") else "abcdefghijklmnopqrstuvwxyz"["abcdefghijklmnopqrstuvwxyz".find(i)+n if 25>"abcdefghijklmnopqrstuvwxyz".find(i)+n else "abcdefghijklmnopqrstuvwxyz".find(i)+n-26] if i.isalpha() else i) for i in s])
# import string
# up = string.ascii_uppercase
# lo = string.ascii_lowercase
# solution = lambda s,n: ''.join([(up[up.find(i)+n if 25>up.find(i)+n else up.find(i)+n-26] if (i in up) else lo[lo.find(i)+n if 25>lo.find(i)+n else lo.find(i)+n-26] if i.isalpha() else i) for i in s])