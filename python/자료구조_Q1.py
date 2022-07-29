#알아볼수 없음 -> 0
#해결방법
#1. 같은 숫자 찾아서 개수 세기
#2. 0개수 세기 
# 1+2 등수 
def solution(lottos, win_nums):
    answer = []
    a=len(set(lottos)&set(win_nums))
    b=zero(lottos)
    answer.append(find(b+a)) #최대
    answer.append(find(a)) #최소
    return answer
def find(a):
    if a==6:
        return 1
    elif a==5:
        return 2
    elif a==4:
        return 3
    elif a==3:
        return 4
    elif a==2:
        return 5
    else: return 6
def zero(lottos):
    count=0
    for i in lottos:
        if i==0:
            count+=1
    return count
            
# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
answer = solution(lottos, win_nums)
print(answer)