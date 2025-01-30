def solution(progresses, speeds):
    res = []
    today = 0
    for progress, speed in zip(progresses, speeds):
        d_day = 100 - progress
        day = d_day//speed + bool(d_day%speed)
        
        if day > today:
            res.append(1)
            today = day
        else:
            res[-1] += 1
    
    return res