def solution(elem):
    # 결과를 저장할 집합 (중복 제거)
    res = set()
    n = len(elem)

    # 부분수열의 길이 1부터 len(elem)까지 반복
    for length in range(1, n + 1):
        # 시작점을 이동하며 부분합 계산
        for start in range(n):
            # 원형 배열 처리
            sub_sum = sum(elem[start:start + length])  # 기본 부분합 계산
            if start + length > n:  # 배열을 초과한 경우
                sub_sum += sum(elem[:(start + length) % n])  # 초과된 부분 추가
            res.add(sub_sum)  # 결과 집합에 추가

    return len(res)  # 고유한 부분합의 개수 반환
