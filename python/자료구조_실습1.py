a=[]
b=True
for i in range(2,1001):
    for j in range(1,i+1):
        if i%j==0:
            b=False
     
    if b==True:
        a.append(i)       
            
print(a)