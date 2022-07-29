def search_while(a,key):
    i=0
    count=0
    while True:
        if i==len(a):
            return -1
        else:
            count+=1
            if a[i]==key:
                return count
        i+=1
        
def search_sentinel(a,key):
    count=0
    b=a.copy()
    b.append(key)
    i=0
    while True:
        if b[i]==key:
            break
        else:
            count+=1
            i+=1
    return -1 if i==len(b) else count

a=[2,5,1,3,9,6,7]

print(search_while(a,7))
print(search_sentinel(a,7))