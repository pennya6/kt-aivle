n=int(input('정수를 입력하세오 : '))
for i in range(1,10):
    for j in range(1,7):
        if i**j==n:
            print(f'{i}**{j}')
        