# 대구 지하철 역명 승하차 인원 분석
import csv

REAL_FILE ='대구교통공사_역별일별시간별 승하차인원_20171231.csv'

# ==========================================
# 1. 파일 불러오기
# ==========================================
def load_real_csv(filename):
    """
    실제 공공데이터 csv  파일을 읽어서 딕셔너리/리스트로 반화하는 함수

    매개변수(파라미터):
        filename : 읽을 파일 이름

    반환값:
        list of dict : 각 요소가 딕셔너리인 리스트

    DictReader() --> csv에서 첫 줄(header, 제목)을 자동으로 키로 사용
    """
    with open(filename, 'r', encoding='cp949') as f:
        reader = csv.DictReader(f)
        return list(reader) #딕셔너리 형태로 읽어서 리스트로 반환-> 반복문에 유리
    
print()
print('='*50)
print('데이터 파일 읽기')
print('='*50)

# ==========================================
# 2. 미리 보기 (3행만)
# ==========================================
# 함수 호출
real_data = load_real_csv(REAL_FILE)
print(f'전체 데이터 : {len(real_data):,}행') # ',(콤마)'는 천단위 구분기호
print()
print('첫 3행 미리보기')
for row in real_data[0:3]:
    print({k:row[k] for k in ['월','일','역명','승하','08시-09시', '일계']})

# ==========================================
# 3. 승차 인원 합계
# ==========================================
def monthly_boarding(data):
    """
    월별 전체 승차 인원 합계를 집계하는 함수

    반환값:
        dict : {'01':합계, '02': 합계, ......}
    """
    montyly ={}
    for row in data:
        if row['승하'] =='승차':
            month = row['월']
            montyly[month] = montyly.get(month, 0) + int(row['일계'])
    return montyly

# ==========================================
# 4. 합계 기준 상위 n개 역
# ==========================================
def top_stations(data, n=5):
    """
    연간 승차 합계 기준 상위 n개 역을 반환
    
    매개변수:
        data: 딕셔너리로 된 리스트
        n: 반환할 역 개수(기본값 5)
    반환값:
        list of tuple: [('역명', 합계),....]
        -> 내림차순 정렬
            sorted()로 값 기준 내림차순 정렬
            key = lambda x: x[1]
            reverse = True
    """
    totals = {}
    for row in data:
        if row['승하'] == '승차':
            station =row['역명']
            totals[station] = totals.get(station, 0) + int(row['일계'])

    sorted_totals = sorted(totals.items(), key = lambda x:x[1], reverse=True)
    return sorted_totals[:n] #상위 n개만 반환

# ==========================================
# 5. 호선별 연간 승차 합계
# ==========================================
def boarding_by_line(data):
    """
    호선별 연간 승차 합계를 집계하는 합수

    반환값:
        dict --> ['1호선':합계, '2호선': 합계, '3호선': 합계]
    
    row['역번호'] --> 해당 역 번호 ex) 1150
                        0번째 글자 추출
                        1 -> 1호선, 2 -> 2호선, 3 -> 3호선
    """
    lines={'1호선': 0, '2호선': 0, '3호선': 0}

    for row in data:
        if row['승하'] == '승차':
            prefix = row['역번호'][0]  # 역번호 중에 첫번째 숫자만 추출, 1 -> 1호선, 2 -> 2호선, 3 -> 3호선
            if prefix == '1':
                lines['1호선'] += int(row['일계'])
            elif prefix == '2':
                lines['2호선'] += int(row['일계'])
            elif prefix == '3':
                lines['3호선'] += int(row['일계'])
    return lines

# ==========================================
# 6. 특정 역의 월별 승차 인원 추이
# ==========================================
def station_monthly(data, station_name):
    """
    특정 역의 월별 승차 인원 추이를 반환하는 함수

    매개변수(파라미터:
        data : 요소가 딕셔너리로 되어 있는 리스트
        station_name : 조회할 역 이름(문자열, 예:'동대구역')
    
    반환값:
        dict: {'01':합계, '02':합계, ...... '12':합계}
    """
    monthly ={}
    for row in data:
        # 여명과 승차 두 조건을 모두 만족하는 행만 처리
        if row['역명'] == station_name and row['승하'] == '승차':
            month = row['월']
            monthly[month] = monthly.get(month,0) + int(row['일계'])
    return monthly

print()
print('='*50)
print('데이터 파일 읽기')
print('='*50)

# ==========================================
# 7. 원하는 역의 결과 확인
# ==========================================

# 분석 1 : 월별 전체 승차 인원
print()
print('[월별 전체 승차 인원]')
# 함수 호출
monthly =monthly_boarding(real_data)
# print(monthly)
for month, count in sorted(monthly.items()):
    print(f'  {month}월: {count:,}명')

print()
# 분석 2 : 연간 승차 Top 7역
print('[연간 승차 Top 7역]')
# 함수 호출
top7 = top_stations(real_data, 7) # 기본값은 5위, 내가 원하는 값 7위
# print(top5)
for rank, (station, count) in enumerate(top7, start=1):
    print(f'{rank}위 {station}: {count:,}명')

print()
# 분석 3 : 호선별 연간 승차 합계
print('[호선별 연간 승차 합계]')
by_line = boarding_by_line(real_data)
# print(by_line)
for line, count in by_line.items():
    print(f'{line}: {count:,}명')

print()
# 분석 4 : 특정 역의 월별 승차 추이
TARGET = input('지하철 역명을 입력해주세요 : ') 
print()
print(f'[{TARGET} 월별 승차 추이]')
# 함수 호출
station_trend = station_monthly(real_data, TARGET)
# print(station_trend)
for month, count in sorted(station_trend.items()):
    print(f' {month}월 {count: ,}명')

# ==========================================
# 8. 결과 나온 것을 csv파일로 저장하여 내보내기
# ===========================================
def save_csv(data, filename):
    """"
    결과로 나온 딕셔너리 리스트를 CSV파일로 저장하는 함수

    매개변수(파라미터):
        data: 저장할  결과 딕셔너리 리스트(list of dict)
        filename : 저장할 파일 이름(문자열)
    DictWriter: 딕셔너리 리스트를 CSV 파일로 쓰는 클래스
    newline='': CSV 모듈이 줄바꿈을 직접 처리하므로 빈 문자열로 설정
                윈도상태에서 빈 줄이 들어갈 가망성이 아주 크다.
    encoding='utf-8-sig' : BOM(Byte Order Mark) 포함 UTF-8
                           엑셀에서 열었을 때 한글이 깨지지 않는다. 메모장에서 깨질수 있음.
    fieldnames : 첫번째 딕셔너리의 키 목록을 헤더로 사용
    writeheader() : 헤더(컬럼명) 한 줄을 먼저 작성
    writerows() : 데이터 전체를 한 번에 작성(줄)
    """
    with open(filename, 'wt', newline="", encoding='utf-8-sig') as f:
        writer =csv.DictWriter(f,fieldnames=data[0].keys())  
        writer.writeheader()    # 헤더(컬럼명) 한 줄을 먼저 작성
        writer.writerows(data)  # 데이터 전체 쓰기
    print(f'저장 완료: {filename} ({len(data)}행)')


result_data =[
    {'월':month, '역명':TARGET, '승차인원': count }
    for month, count in sorted(station_trend.items())
]

# 저장 파일명
OUTPUT_FILE = f'{TARGET}_월별승차추이.csv'

# 함수 호출
save_csv(result_data,  OUTPUT_FILE)

print()
print(f'저장된 파일을 확인해보세요 : {OUTPUT_FILE}')