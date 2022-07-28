left=int(input('left : '))
right=int(input('right : '))

def solution(left,right):
    a=[] #짝수
    b=[] #홀수
    for i in range(left,right+1):
        n=[] #개수
        for j in range(left):
            for k in range(right+1):

                if j*k==i:
                    n.append(j)
                    n.append(k)
        
        sn=len(set(n))
        if sn%2==0:
            a.append(i)
        else:
            b.append(i)
    
    if len(a)>0:
        sum=a[0]
        for i in range(1,len(a)):
            sum+=a[i]
    if len(b)>0:      
        for i in range(len(b)):
            sum-=b[i]
    
    return sum

print(solution(left,right))