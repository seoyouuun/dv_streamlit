import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="여시코껭이의 대시보드",
    page_icon="🎈",
    layout="wide"
)

# 2. 메인 화면 제목
st.title("🏠 메인 홈")
st.markdown("""
반가워요! **여시코껭이 서여이**의 스트림릿 실습 페이지입니다.  
왼쪽 **사이드바**를 눌러도 되고, 아래 **버튼**을 눌러서 이동할 수도 있어요!
""")

st.divider() # 구분선

# 3. 메뉴 바로가기 버튼 만들기
st.subheader("📂 학습 메뉴 바로가기")

# 컬럼으로 버튼을 나란히 배치
col1, col2 = st.columns(2)

with col1:
    st.info("📖 텍스트와 미디어 다루기")
    # 캡처에 있는 파일 이름 그대로 적었습니다!
    if st.button("1. 텍스트_미디어 페이지로 이동"):
        st.switch_page("pages/1_text_media.py")

with col2:
    st.success("📊 데이터와 그래프 그리기")
    # 캡처에 있는 파일 이름 그대로 적었습니다!
    if st.button("2. 데이터_그래프 페이지로 이동"):
        st.switch_page("pages/2_데이터_그래프.py")

st.divider()

# 추가 버튼 (레이아웃, 위젯 등)
st.write("다른 기능들도 확인해보세요 👇")
col3, col4 = st.columns(2)

with col3:
    if st.button("3. 레이아웃 페이지로 이동"):
        st.switch_page("pages/3_레이아웃.py")

with col4:
    if st.button("4. 위젯 페이지로 이동"):
        st.switch_page("pages/4_위젯.py")

# 5. 마무리
st.caption("Created by 여시코껭이 서여이")
