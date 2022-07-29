def reverse(a):
    for i in range(len(a)//2):
        a[i],a[n-i-1]=a[n-i-1],a[i]
        
print('리스트를 역순으로 출력합니다.')
x=[]
while True:
    q=input('값을 입력하세요 : ')
    if q=='End':
        break
    x.append(int(q))
print('리스트를 역순으로 출력합니다.')
n=len(x)
reverse(x)
print(x)