def search(x,a):
    pl=0
    pr=len(a)-1
    while True:
        pc=(pl+pr)//2
        if x[pc]==a:
            return pc
        elif x[pc]<a:
            pl=pr+1
        else:
            pr=pc-1
        if pl>pr:
            break
    return -1
        
n=int(input('원소 수를 입력하세요. : '))
x=[]
for i in range(n):
    q=input(f'x[{i}]값을 입력하세요 : ')
    x.append(q)
a=input('검색할 값을 입력하세요 : ')
index=search(x,a)
if index==-1:
    print("값이 없습니다.")
else:
    print(f"{index}에 있습니다.")