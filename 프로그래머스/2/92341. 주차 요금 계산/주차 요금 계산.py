from collections import defaultdict

def solution(fees, records):
    '''
    args
        fees (List[int]): len(fees) == 4
            fees[0] = 기본 시간(분)
            1 ≤ fees[0] ≤ 1,439
            fees[1] = 기본 요금(원)
            0 ≤ fees[1] ≤ 100,000
            fees[2] = 단위 시간(분)
            1 ≤ fees[2] ≤ 1,439
            fees[3] = 단위 요금(원)
            1 ≤ fees[3] ≤ 10,000
        records (List[str]): 1 <= len(records) <= 1000, 하루동안의 입/출차 기록
            "시각 차량번호 내역" 형식의 문자열, 시각을 기준으로 오름차순 정렬
            "HH:MM \d{4} (IN|OUT)"
            다음날 출차되는 경우는 입력으로 주어지지 않음, 23:59 입차는 주어지지 않음
            없는 차량이 출차되는 경우/있는 차량이 재입차 되는 경우는 주어지지 않음
    return List[int]
    '''
    def _calc(t, fees=fees):
        if t > fees[0]:
            return fees[1] + (t - fees[0] + fees[2] - 1)//fees[2] * fees[3]
        return fees[1]
    
    check_in = {}
    cars = defaultdict(int)
    
    for record in records:
        t, k, io = record.split()
        h, m = map(int, t.split(":"))
        t = h*60 + m
        
        if io == "IN":
            check_in[k] = t
        else:
            t -= check_in.pop(k)
            cars[k] += t
        
    for k, v in check_in.items():
        cars[k] += 1439 - v
    
    return [_calc(cars[k]) for k in sorted(cars.keys())]