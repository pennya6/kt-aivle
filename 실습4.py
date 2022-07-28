n=int(input('정수를 입력하세오 : '))
for i in range(1,n):
    for j in range(2,7):
        if i**j==n:
            print(f'{i}**{j}')
        