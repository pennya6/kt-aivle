def solution(arr):
    if len(arr)<2:
        return -1
    arr.pop(arr[min(arr)])
    return arr
arr = [4, 3, 2, 1]
answer = solution(arr)
print(answer)