a=int(input("a:"))
b=a
sum=0
cycle=1
for i in range(20):
    if b>0 and b<10:
        b='0'+str(b)
        sum=int(b)
    else:
        sum=b%10+b//10
    new_a=str(b%10)+str(sum%10)
    
    print('n:',new_a)
    print('b:',b)
    print('a:',a)
    
    if int(new_a)==a:
        break
    else:
        b=int(new_a)
    cycle=cycle+1
print(cycle)