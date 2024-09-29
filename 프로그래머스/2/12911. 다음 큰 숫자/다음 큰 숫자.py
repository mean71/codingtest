
def solution(n):
    N = n
    while True:
        N += 1
        nN = [n,N]
        nN1 = [0, 0]
        for i in range(2):
            print(i)
            while nN[i] > 0:
                if nN[i]%2:
                    nN1[i] += 1
                nN[i]=nN[i]//2
        print(nN1)
        if nN1[0] == nN1[1]:
            return N
print(solution(78))