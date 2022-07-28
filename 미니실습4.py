area=int(input('넓이를 입력하세요 : '))
for i in range(1,area+1):
    if area%i:
        continue
    print(f'{i}*{area//i}')