def solution(x):
    score, temp_n = [], ""
    
    for c in x:
        if c.isnumeric():
            temp_n += c
        elif c.isalpha():
            score.append(int(temp_n)**(1 + (c=="D") + 2*(c=="T")))
            temp_n = ''
        elif c == "#":
            score[-1] *= -1
        elif c == "*":
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
                
    return sum(score)