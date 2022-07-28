company=input('수도회사를 입력하세요(A/B) : ')
using=int(input('수도 사용량을 입력하세요 : '))
charge=0
if company=='A':
    charge=using*100
elif company=='B':
    if using<=50:
        charge=using*150
    else:
        charge=using*75
print(f'요금은 {charge}입니다.')
        