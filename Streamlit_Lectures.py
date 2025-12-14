import streamlit as st

st.set_page_config( #페이지 설정
  page_title="하교수의 Streamlit", # 페이지 Tab의 타이틀
  page_icon="", #페이지 Tab의 아이콘
  layout="wide", #페이지 레이아웃: centered, wide
  #사이드바 초기 상태: auto, collapsed, expanded
  initial_sidebar_state="expanded",
  #페이지 오른쪽 상부의 메뉴에 추가할 메뉴 항목: Get help, Report a bug, About
  menu_items={
  'Get help': "https://docs.streamlit.io", # URL만
  'Report a bug': "https://streamlit.io", #URL만
  'About': "##하정훈 교수\n - [홍익대학교 산업·데이터공학과]
   }
)

#사이드바 설정
st.sidebar.title('다양한 사이드바 위젯들')

st.sidebar.checkbox('외국인 포함'
st.sidebar.checkbox('고령인구 포함')
st.sidebar.divider() # 구분선
st.sidebar.radio('데이터 타입', ['전체', '남성', '여성'])
st.sidebar.slider('나이', 0, 100, (20, 50))
st.sidebar.selectbox('지역', 【'서울', '경기', '인천', '대전', '대구', '부산', '광주'])
