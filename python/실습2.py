n=int(input('몇 번 출력할 지 입력하시오:'))
for i in range(n):
    if i%2==0:
        print('+',end='')
    else:
        print('-',end='')