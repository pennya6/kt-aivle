def solution(n, s):
    a=[]
    b=[]
    
    for i in range(1,s//2+1):
        a.append([i,s-i])
    for i in range(len(a)):
        b.append(a[i][0]*a[i][1])
    if len(b)>0: return a[b.index(max(b))]
    else: return -1

n = 2
s = 8

answer = solution(n, s)
print(answer)