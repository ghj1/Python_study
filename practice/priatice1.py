prompt = '''[커피 자동주문 머신 메뉴]
-------------------------------
-아메리카노는 2500원 
-카페라떼는 3000원
-카푸치노는 3000원 
입니다. 원하시는 커피종류와 잔수를 입력하세요.
--------------------------------
'''

print(prompt)

coffe1 = int(input('아메리카노 몇잔? '))
coffe2 = int(input('카페라떼 몇잔? '))
coffe3 = int(input('카푸치노 몇잔? ')) 

total = coffe1*2500 +coffe2*3000 + coffe3*3000
print(f'지불할 총 금액은 {total}원 입니다.')

money = int(input('돈을 넣어주세요: '))

if money > total: 
    print(f'거스름돈은 {money - total}원 입니다.')
elif money == total:
    print('결제가 완료 되었습니다.')
else: 
    print(f'입력한 금액이 부족합니다. {total - money}원을 더 넣어주세요.')
