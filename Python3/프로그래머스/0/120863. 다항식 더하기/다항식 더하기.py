def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x,n = 0,0
    for i in polynomial:
        
        if 'x' == i[-1]:
            if i[:-1]:
                x += int(i[:-1])
            else:
                x += 1
        elif i.isnumeric():
            n += int(i)
    if x > 1:
        if n:
            return f"{x}x + {n}"
        else:
            return f"{x}x"
    elif x == 1:
        if n:
            return f"x + {n}"
        else:
            return "x"
    else:
        return f"{n}"