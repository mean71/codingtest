def solution(schedules, timelogs, startday) -> int:
    '''
    args
        schedules(List[int]): 출근 희망시간 700 <= hhmm <=1100
        timelogs(List[List[int]]): 일주일 출근 기록 600 <= timelogs[i][j] <= 2359
        startday(int): 시작 요일 1:월 - 7:일
    return res(int): 출근 희망시간에 늦지않은 직원 수
    '''
    schedules = [(time//100 + (time%100 >= 50))*100 + (time%100 + 10)%60 for time in schedules]
    res = 0
    
    for i, logs in enumerate(timelogs):
        if all(schedules[i] >= t for j,t in enumerate(logs) if (startday + j - 1)%7 < 5):
            res += 1
    
    return res