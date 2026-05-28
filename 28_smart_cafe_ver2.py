# 함수 정의
def payment():
    total = 0  # 지불해야 할 금액
    while True:
        order = input('주문 메뉴 입력(0:종료) ')
        if order == '0':
            break
        count = int(input('수량 입력 : '))
        for i in menu:
            if i[0] == order:
                result.append([i[0], i[1], count])
    for i in result: # ['에스프레소',2000, 3]
        total += i[1] * i[2]
    return total



menu= [['에스프레소',2000,'커피'],['아메리카노',2500,'커피'],['카푸치노',3000,'커피'],
       ['카페라떼',3000,'커피'],['모카라떼',3500,'커피'],['바닐라라떼',3500,'커피'],
       ['소이라떼',3500,'커피'],['피넛라떼',3700,'커피'],['토피넛라떼',3700,'커피'],
       ['화이트모카',3700,'커피'],['카라멜마끼아또',4000,'커피'],['프라프치노',4000,'커피'],
       ['핫초코',3500,'음료'],
       ['레몬에이드',3500,'음료'],['청포도에이드',3500,'음료'],['자몽에이드',3500,'음료'],
       ['스무디',3500,'음료'],['망고스무디',3500,'음료'],['딸기스무디',3500,'음료'],
       ['초코쿠키',2000,'디저트'],['화이트쿠키',2000,'디저트'],['피넛쿠키',2000,'디저트'],
       ['당근케이크',5000,'디저트'],['초코케이크',5000,'디저트'],['치즈케이크',5000,'디저트']]

result = []
print('[스마트 카페 메뉴 목록]')
print()
for i in menu:
    print(i[0], end=' ') # i --> ['에스프레소', 2000, '커피']
print()

while True:
    choice = int(input('1.가격별 메뉴 조회  2.종류별 메뉴 조회  3.주문  0.종료 : '))
    result = []
    if choice < 0 or choice > 3:
        print('없는 번호! 다시 입력하세요!')
        continue
    elif choice == 1:
        min, max = eval(input('최저가격, 최고가격 입력(예: 1000,2000) '))
        for i in menu:
            if min <= i[1] <= max:
                result.append(i[:2])
    elif choice == 2:
        category = input('종류별 메뉴 입력(예: 커피, 음료, 디저트 중 하나) ')
        for i in menu:
            if i[2] == category:
                result.append(i[:2])
    elif choice == 3:
        total = payment()  # 함수 호출
        print(f'주문 내역 확인 : {result}')
        print(f'지출할 총금액 : {total}원\n')
        continue
    elif choice == 0:
        print('스마트 카페 메뉴조회 시스템 종료!')
        break

    print('<입력 조건의 메뉴 목록>')
    print(result)
    print()