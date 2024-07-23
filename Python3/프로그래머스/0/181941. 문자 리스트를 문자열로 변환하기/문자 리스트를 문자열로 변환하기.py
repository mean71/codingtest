def solution(arr):
    while not(answer := '') and 1<=len(arr)<=200 and (all(arr[x].islower()) for x in range(len(arr))):answer = ''.join(arr);break
    return answer