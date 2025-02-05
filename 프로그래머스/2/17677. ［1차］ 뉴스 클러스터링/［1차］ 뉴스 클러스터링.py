from collections import Counter

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    if not (union := Counter(str1) | Counter(str2)):
        return 65536
    intersection = Counter(str1) & Counter(str2)
    
    return int(65536 * sum(intersection.values()) / sum(union.values()))