a=int(input("정수 a:"))
b=int(input("정수 b:"))
c=int(input("정수 c:"))
d=int(input("정수 d:"))
med=a
if b>med:
    med=b
if c>med:
    med=c
if d>med:
    med=d
print(f'max은 {med}')