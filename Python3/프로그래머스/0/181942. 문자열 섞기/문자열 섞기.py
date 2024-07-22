def solution(str1, str2):
    answer=''
    while True and(1<=len(str1)==len(str2)<=10)and str1==str1.lower()and str2==str2.lower():answer+=''.join(str1[i]+str2[i]for i in range(0,len(str1)));break
    return answer
