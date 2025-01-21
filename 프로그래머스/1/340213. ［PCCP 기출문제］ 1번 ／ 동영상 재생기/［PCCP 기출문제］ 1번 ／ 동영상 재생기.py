def solution(v_len, pos, op_s, op_e, cmds):
    """동영상 재생 위치 조정 함수
    사용자의 명령어(cmds)에 따라 동영상 재생 위치를 조정
    - "prev": 10초 전으로 이동 (단, 10초 미만일 경우 0초로 설정)
    - "next": 10초 후로 이동 (단, 남은 시간이 10초 미만일 경우 마지막 위치로 설정)
    - 오프닝 구간(op_s ≤ pos < op_e)에 있을 경우 op_e 위치로 이동

    Argus:
        v_len (str): "MM:SS" 동영상의 전체 길이(초)
        pos (str): "MM:SS" 기능 수행 전 현재 위치(초)
        op_s (str): "MM:SS" 오프닝 시작 위치(초)
        op_e (str): "MM:SS" 오프닝 종료 위치(초)
        cmds (List[str]): 수행할 명령어 목록 (["prev", "next"] 중 하나)
    Return:
        str: 변경된 재생 위치를 "MM:SS" 형식의 문자열로 반환
    """
    v_len = int(v_len[:2])*60 + int(v_len[-2:])
    time = int(pos[:2])*60 + int(pos[-2:])
    op_s = int(op_s[:2])*60 + int(op_s[-2:])
    op_e = int(op_e[:2])*60 + int(op_e[-2:])
    
    time = op_e if op_s <= time < op_e else time
    
    for cmd in cmds:
        time += 10 if cmd=="next" else -10
        time = min(max(0, time), v_len)
        time = op_e if op_s <= time < op_e else time

    return f"{str(time//60).zfill(2)}:{str(time%60).zfill(2)}"