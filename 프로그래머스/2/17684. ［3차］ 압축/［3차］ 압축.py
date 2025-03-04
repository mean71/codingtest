import string

def solution(msg):
    '''
    LZW압축
    1. 길이가 1인 모든단어를 포함하도록 사전 초기화
    2. 현재 입력과 일치하는 가장 긴 문자열 w를 찾음
    3. w에 해당하는 사전의 색인번호를 출력, 입력에서 w제거
    4. 입력에서 처리 되지 않은 다음 글자가 남아있다면 (c), w+c 에 해당하는 단어를 사전등록
    5. 2부터 반복
    영문대문자만 처리
    args
        msg (str): 압축할 "[A-Z]+" 문자열
    return
        List[int]: 압축된 사전 색인번호 배열
    '''
    dic = {k:v for v, k in enumerate(string.ascii_uppercase, 1)}
    res = []
    w = ""
    
    for c in msg:
        wc = w+c
        if wc in dic:
            w = wc
        else:
            res.append(dic[w])
            dic[wc] = len(dic) + 1
            w = c
    if w:
        res.append(dic[w])
    
    return res

    # l,r = 0,1

    # while True:
    #     while msg[l:r] in dic:
    #         r += 1
    #         if r > len(msg):
    #             res.append(dic[msg[l:r-1]])
    #             return res
    #     else:
    #         dic[msg[l:r]] = len(dic) + 1
    #         res.append(dic[msg[l:r-1]])
    #         l = r-1