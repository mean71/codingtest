while True:
    ABC = list(map(int, input().split()))
    if ABC[0]*ABC[1]*ABC[2] and ABC[0]+ABC[1] > ABC[2]:
        a,b,c = map(lambda x: x**2, sorted(ABC))
        print('right' if a+b == c else 'wrong')
    else: break