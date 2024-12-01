def solution(N,s):
    failure_rate = []
    for i in range(1, N+1):
        challenger = complet = 0
        for n in s:
            if n >= i:
                challenger += 1
                if n > i:
                    complet += 1
        
        try:success_rate = complet/challenger
        except:success_rate = 1
        failure_rate.append((success_rate, i))
    return [j for i,j in sorted(failure_rate)]