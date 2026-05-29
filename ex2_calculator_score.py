result = []
total = 0
count = 0
average = 0
while True:
    info = int((input('1.수강 강좌정보 입력 2.평균평점 확인 0.종료:')))

    if info < 0 or info > 2:
        print('없는 번호! 다시 입력하세요!')
        continue
    
    elif info == 1:
        print("<수강 강좌정보 입력>")

        while True:
            subject = input('과목명(0:종료):')

            if subject == '0':
                print("<수강 강좌 입력종료>")
                break

            score_int = float(input('학점 수:'))
            total += score_int
            count += 1
            average = total/count
            score_text = input('취득학점(A,B,C,F):')

            result.append((subject, score_int, score_text))
        print('*'*50)
        print('  '+'<수강 강좌 목록>')
        print('과목명'+'  '+'학점수'+'  '+'학점')
        print('-'*20)
        for sub, score, grade in result:
            print(sub, score, grade)

        print(f'평균평점: {average:.2f}')
        
    elif info == 0:
        print('초간단 평점평균 계산 시스템 종료!')
    break

    
