def search(a, key):
    pl = 0
    pr = len(a)-1
    
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        
        if pl > pr:
            break
    return -1
def solution(store, customer):
    answer = []
    for i in customer:
        a=search(store,i)
        if a!=-1:
            answer.append('yes')
        else: answer.append('no')
            
    return answer

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)