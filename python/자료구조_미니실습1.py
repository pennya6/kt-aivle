def min_of(a):
    min=a[0]
    for i in range(len(a)):
        if a[i]<min:
            min=a[i]
    return min

t=(4,5,5.6,2,3.14,1)
s='string'
a=['DTS','AAC','FLAC']
print(min_of(t))
print(min_of(s))
print(min_of(a))