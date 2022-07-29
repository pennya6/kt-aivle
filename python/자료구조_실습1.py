a=[]
b=True
for i in range(2,1001):
    b=True
    for j in range(2,i):
        if i%j==0:
            b=False
            break
    if b==True:
        a.append(i)       
            
print(a)