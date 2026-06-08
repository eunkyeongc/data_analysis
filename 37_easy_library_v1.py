# [0]도서관코드, [1]도서관명, [2]주소, [3]상세주소, [4]전화번호, [5] 팩스번호, [6]홈페이지주소, [7]개관시간, [8]휴관일

# csv 라이브러리 불러오기
from csv import *  # csv 라이브러리 안 모든 함수를 가져와라. 호출 시 함수명으로 호출 가능

file = open('library.csv', 'r')
read_file = reader(file) #csv안의 reader함수를 불러온다. -> file 객체 내용 다 읽기

library_list = []
for line in read_file:
    library_list.append(line)
file.close()

while True:
    search_word = input('\n검색어 입력(종료:0) : ')
    if search_word == '0':
        print('\n[도서관 정보 검색 시스템 종료]')
        break
    print('\n [도서관 정보 검색 결과]')
    for line in library_list:
        if search_word in line[1]:  # 찾는 단어가 line[1](도서관명)에 포함되어 있니?
            print(f'{line[1]} / {line[2]} / {line[4]}') #도서관명 / 주소 / 전화번호


