def solution(l):
    b = "aya", "ye", "woo", "ma"
    bb = [w*2 for w in b]
    return sum(not j.replace(b[0],' ').replace(b[1],' ').replace(b[2],' ').replace(b[3],' ').strip() for j in l if all(sb not in j for sb in bb))