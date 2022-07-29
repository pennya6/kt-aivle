def search(a, key):
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1
        
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