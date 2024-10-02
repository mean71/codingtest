def solution(s):
    str=''
    sniffling = 0
    for i,j in enumerate(s):
        if j.isalpha():
            if sniffling:
                str += s[i].lower()
                sniffling = 0
            else:
                str += s[i].upper()
                sniffling = 1
        else:
            str += ' '
            sniffling = 0
    return str