#해결방법
# numbers 에 있는 숫자는 0->1로 바꾸기 
# 0인 값만 찾아서 더하기
def solution(numbers):
    number=[0,1,2,3,4,5,6,7,8,9]
    check=[0,0,0,0,0,0,0,0,0,0]
    answer=0
    for i in range(len(numbers)):
        index=numbers[i]
        check[index]=1
    print(check)
    for i in range(len(check)):
        if check[i]==0:
            answer+=number[i]
    return answer

numbers = [5,8,4,0,6,7,9]
answer = solution(numbers)
print(answer)