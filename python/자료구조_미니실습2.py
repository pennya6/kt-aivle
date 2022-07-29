def reverse(a):
    for i in range(len(a)//2):
        a[i],a[n-i-1]=a[n-i-1],a[i]
        

print('리스트를 역순으로 출력합니다.')
n=int(input('원소 수를 입력하세요. : '))
x=[]
for i in range(n):
    q=int(input(f'x[{i}]값을 입력하세요 : '))
    x.append(q)
print('리스트를 역순으로 출력합니다.')
reverse(x)
print(x)