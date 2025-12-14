import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="여시코껭이의 대시보드",
    page_icon="🎈",
    layout="wide"
)

# 메인 화면 제목
st.title("🏠 환영합니다!")

st.markdown("""
안녕하세요, **여시코껭이 서여이**님!  

Streamlit의 **멀티 페이지 앱(Multi-page App)**은 왼쪽 **사이드바**에 자동으로 메뉴를 생성합니다.  

👈 **사이드바를 열고** 학습할 페이지를 선택해 주세요.
""")

st.divider()

st.info("💡 **팁:** pages 폴더에 있는 파일 이름 앞에 숫자를 붙이면 (예: 1_file.py) 사이드바에 순서대로 정렬됩니다.")

# 마무리
st.caption("Created by 여시코껭이 서여이")
