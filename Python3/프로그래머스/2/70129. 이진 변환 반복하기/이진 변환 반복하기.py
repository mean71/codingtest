def solution(s):
    a=0
    zero,count = 0,0
    while s != '1':
        zero += s.count('0')
        count += 1
        s = '1'*s.count('1')
        binary = len(s)
        temp = ''
        while binary//2 or binary%2:
            print(binary)
            if binary%2:
                temp += '1'
            else:
                temp += '0'
            binary = binary//2
            print(binary)
        s = ''.join(reversed(temp))
    return [count, zero]