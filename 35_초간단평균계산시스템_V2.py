# 초간단 평점평균 계산 시스템
# - 초간단 평점평균 계산 시스템은 수강한 강좌의 학점수, 취득학점을 입력하면 평점평균을 계산하여 출력하는 시스템입니다. 
# - 즉, 수강한 강좌를 반복하여 입력하고, 입력 완료 후 평점 평균을 계산해 주는 프로그램입니다.

# < 요구사항 >
# - 수강 강좌정보 입력 화면에서 과목명, 학점수, 취득학점을 반복하여 입력받습니다.
# - 더 이상 입력할 강좌가 없으면 입력 화면을 종료합니다.
# - 수강 강좌정보 입력 후 평점평균 확인을 입력하면 평점평균을 계산하여 출력합니다.

# < 추가 요구사항 >
# - 총 등록학기를 입력받아 8학기 이상이면 졸업학기 충족, 미만이면 학기 부족을 출력합니다.
# - 총 학점수를 입력받아 120학점 이상이면 졸업학점 충족, 미만이면 졸업학점 부족을 출력합니다.
# - 총 평균평점을 입력받아 2.5학점 이상이면 졸업 평균평점 충족, 미만이면 졸업 평균평점 부족을 출력합니다.

def subject():      #수강 강좌정보 입력 화면
    while True:
        title = input('과목명(0:종료) : ')
        if title == '0':
            break
        credit = int(input('학점 수 : '))
        grade = input('취득학점(A, B, C, F) : ')
        course.append([title, credit, grade])

def avg_grade():    #평점 평균을 계산
    total = 0
    result = 0
    for i in course:
        if i[2] == 'A':
            total += i[1]
            result += i[1]* 4.5
        elif i[2] == 'B':
            total += i[1]
            result += i[1]* 3.5 
        elif i[2] == 'C':
            total += i[1]
            result += i[1]* 2.5  
        elif i[2] == 'F':
            total += i[1]
    return result/total    
    
def graduate():
    tot_semester =(int(input('총 등록 학기수 입력 :')))
    if tot_semester >= 8:
        print('졸업학기 충족 완료')
    else:
        print(f'{8-tot_semester}학기 부족')

    tot_credit = int(input('\n수강 완료 학점수 입력: '))

    if tot_credit >= 120:
        print('졸업학점 충족 완료')
    else:
        print(f'{120-tot_credit}학점 부족')   

    tot_grade = float(input('\n총 평균평점 입력: '))
    if tot_grade >= 2.5:
        print('졸업 평균평점 충족 완료')
    else:
        print(f'{2.5-tot_grade}평균평점 부족')   

course =[]
while True:
    choice =int(input('1.수강 강좌정보 입력 2.평균평점 확인 3.졸업여건 확인 0.종료:'))
    if choice < 0 or choice >3:
        print('없는 번호!')
        continue

    elif choice == 1:
        print('\n< 수강 강좌정보 입력 >')
        subject()   #함수 호출
        print('< 수강 강좌정보 입력 종료 > \n')

    elif choice == 2:
        print('\n< 수강 강좌 목록 >')
        print('과목명\t학점수\t학점')
        print('-' * 20)
        gpa = avg_grade() #함수 호출
        for c in course:
            print(f'{c[0]}\t{c[1]}\t{c[2]}')
        print(f'\n 평균평점 : {gpa:.2f}\n')

    elif choice == 3:
        print('\n< 졸업 여건 확인 >')
        graduate()
    elif choice == 0:
        print('초간단 평점평균 계산 시스템 종료!')
        break