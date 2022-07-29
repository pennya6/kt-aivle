def solution(arr):
    answer = []
    a=arr[0]
    answer.append(a)
    for i in range(1,len(arr)):
        if arr[i]!=a:
            a=arr[i]
            answer.append(a)
    return answer

#arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)