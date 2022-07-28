a=int(input("a:"))
sum=0
cycle=0
for i in range(10):
    if a>0 and a<10:
        a='0'+str(a)
        sum=int(a)
    else:
        sum=a%10+a//10
    new_a=str(a%10)+str(sum%10)
    
    print(new_a)
    if new_a==a:
        break
    else:
        a=int(new_a)
    cycle=cycle+1
print(cycle)