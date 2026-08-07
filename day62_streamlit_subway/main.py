"""
2026. 08. 05. 
day62_streamlit_subway/main.py

입력 데이터 : day62_streamlit_subway/input/subway_long.csv
Streamlit으로 만드는 “대구 지하철 승하차 통합 대시보드” 실습

실행 방법: streamlit run main.py

"""

import sys
import os
import streamlit as st

# pages_src폴더를 파이썬의 import 경로(sys.path)에 직접 추가한다.--> streamlit에서 지원이 안되어서 직접 경로 설정.
sys.path.append(os.path.join(os.path.dirname(__file__), 'pages_src'))

st.set_page_config(
    page_title =  '대구 지하철 승하차 통합 대시보드',
    page_icon ='🚇',    # AI에게 지하철이모지 검색 요청 후 복사하여 붙여넣기
    layout = 'wide'     # 화면을 넓게 사용
)

# --- 페이지 등록 ---
# st.page(파일경로, title=사이드바 표시 이름, icon = 아이콘, default = True)
#   - 파일 경로는 상대 경로. main.py 기준
#   - defalut = True인 페이지가 앱을 처음 열었을 때 보이는 화면이 된다.
home_page = st.Page('pages_src/home.py', title='홈', icon='🏡', default=True)
explore_page = st.Page('pages_src/explore.py', title='역별 탐색', icon='🚏')
search_page = st.Page('pages_src/search.py', title='검색', icon='🔍')
trend_page = st.Page('pages_src/trend.py', title='기간, 시간대 추이', icon='📈')
about_page = st.Page('pages_src/about.py', title='소개', icon='🎤')

# ---  사이드바에 페이지 연결 : 각 섹션 제목이 함게 표시된다. 딕셔너리 형태로...
pg = st.navigation({
    '메인' : [home_page],
    '데이터 탐색': [explore_page, search_page, trend_page],
    '기타': [about_page],
})

# pg.run() : 사용자가 사이드바에서 클리한 페이지의 코드를 실제로 실행한다.
#            코드 아래로는 아무것도 입력되어 있지 않아야 한다.
#            실제 화면 구성은 각 페이지 파일이 담당하게 된다.
pg.run() 


