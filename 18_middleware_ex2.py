# 도서관 자석 예약 시스템
# 1. 회원등급 - 정회원, 우수회원 --> 예약 권한 부여
#                   나머지 등급 --> 예약 권한 없음
# 2. 좌석예약 - 00번 좌석이 예약이 완료되었습니다.!
# 3. main - 회원등급 입력 --> 좌석 번호를 입력 --> 1, 2번에 따라서 결과

def reserve_seat(seat_number):
    if 1 <= seat_number <=50 :
        print(f'{seat_number})번 좌석 예약이 완료되었습니다!')
    else :
        print('유효하지 않은 좌석 번호입니다')
def check_membership(grade):
    if grade == '정회원' or grade == '우수회원':
        print('예약 권한 확인 완료!')
        return True
    else :
        print("예약 권한이 없음")
        return False

if __name__ == '__main__':
    grade = input('회원 등급을 입력하세요(준회원/정회원/우수회원) : ')
    if check_membership(grade):  # 함수 호출 --> reture 값이 True/Fale
        seat_number = int(input('좌석 번호를 입력하세요 : '))
        reserve_seat(seat_number) # 함수 호출 --> reture 값이 없음.

        """
**main 코드를 작성하세요.**

- `while` 루프로 아래 메뉴를 반복 실행합니다.
    - `1` 입력 시: 회원 등급과 좌석 번호를 입력받아 두 미들웨어가 모두 `True` 일 때만 `reserve_seat()` 실행
    - `2` 입력 시: `show_reserved()` 실행
    - `3` 입력 시: 종료 메시지 출력 후 루프 종료
- ※ 좌석 번호는 `int()` 로 변환하여 사용하세요.

        """

