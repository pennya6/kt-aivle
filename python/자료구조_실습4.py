n=int(input('원소 수를 입력하세요. : '))
x=[]
for i in range(n):
    q=input(f'x[{i}]값을 입력하세요 : ')
    x.append(q)
max=0
min=0
for i in range(len(x)):
    if x[max]<x[i]:
        max=i
    if x[min]>x[i]:
        min=i
print(min)
print(max)