a=input("숫자로 이루어진 문자열을 입력하세요 : ")
a_n=[]
for i in range(0,len(a)):
    a_n.append(a[i:i+1])
a_n=sorted(a_n)
if a_n[0]=='0':
    sum=int(a_n[0])+int(a_n[1])
    for i in range(2,len(a_n)):
        sum*=int(a_n[i])
else:
    sum=int(a_n[0])
    print(a_n)
    for i in range(1,len(a_n)):
        sum*=int(a_n[i])
    
print(sum)