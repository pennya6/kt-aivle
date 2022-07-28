from re import A


a=int(input("정수 a:"))
b=int(input("정수 b:"))
if a>b:
    a,b=b,a
sum=0
for i in range(a,b+1):
    if i<b+1:
        print(f'+{i}',end="")
    sum+=i
print(f'={sum}')