def electricPay(using):
    charge=0
    if using <100:
        charge=410+using*60.7
    elif using >= 100 and using<200:
        charge=910+100*60.7+(using-100)*125.9
    else:
        charge=1600+100*60.7+100*125.9+(using-200)*187.9
    a=charge*0.1
    b=charge*0.037
    return int(charge+a+b)
using=int(input("사용량을 입력하세요 : "))
print(electricPay(using))
    
    