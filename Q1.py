a=int(input('a:'))
b=int(input('b:'))
a_n=[]
b_n=[]
for i in range(1,a*b):
    a_n.append(i*a)
for i in range(1,a*b):
    b_n.append(i*b)
print(min(set(a_n)&set(b_n)))