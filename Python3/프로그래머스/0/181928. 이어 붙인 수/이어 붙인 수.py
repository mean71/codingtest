def solution(num_list):
    even, Odd = '',''
    for i in num_list:
        if i%2==0:
            even += str(i)
        else:
            Odd += str(i)
    return int(even)+int(Odd)