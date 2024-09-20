import string
up = string.ascii_uppercase
lo = string.ascii_lowercase
def solution(s, n):
    return ''.join([(up[up.find(i)+n if 25>up.find(i)+n else up.find(i)+n-26] if (i in up) else lo[lo.find(i)+n if 25>lo.find(i)+n else lo.find(i)+n-26] if i.isalpha() else i) for i in s])