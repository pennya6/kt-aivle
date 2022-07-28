a=int(input('a:'))
b=int(input('b:'))
a_n=[]
b_n=[]
for i in range(a):
    for j in range(a):
        if i*j==a:
            a_n.append(i)
for i in range(b):
    for j in range(b):
        if i*j==b:
            b_n.append(i)
print(a_n)
print(b_n)
print(max(set(a_n)&set(b_n)))