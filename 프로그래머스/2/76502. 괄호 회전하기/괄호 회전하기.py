def solution(s):
    parenth = {"]":"[", ")":"(", "}":"{"}
    count = 0
    for x in range(len(s)):
        check = []
        for c in s[x:] + s[:x]:
            if check and c in parenth and check[-1] == parenth[c]:
                check.pop()
            else:
                check.append(c)
        count += (not check)
    return count