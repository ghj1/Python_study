import random

print("** 이번주 1등 로또 당첨 번호는? **")

def lottoNumber():
    return random.randrange(1,46)

lotto = []
num = 0

if __name__ == '__main__':
    print("로또번호")
    while True:
        num = lottoNumber()
        if lotto.count(num) ==0:
            lotto.append(num)
        if len(lotto) >= 6:
            break 
    print("로또 번호 -> ", end= "")
    lotto.sort()
    for i in lotto:
        print('%d  ' %i, end = '')

