def solution(s):
    n,t = '',''
    numbers = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4',
               "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    for i,j in enumerate(s):
        if j.isnumeric():
            n += j
        else:
            t += j
            if t in numbers:
                n+= numbers[t]
                t=''
    return int(n)