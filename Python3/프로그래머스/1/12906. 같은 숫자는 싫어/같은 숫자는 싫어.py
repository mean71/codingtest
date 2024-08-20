def solution(arr):
    x = [arr[0]]
    for i in range(0,len(arr)-1):
        if arr[i] != arr[i+1]:
            x.append(arr[i+1])
    return x