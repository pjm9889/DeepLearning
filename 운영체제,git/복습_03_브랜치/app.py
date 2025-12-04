# app.py
import streamlit as st
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="우리 팀 대시보드",
    page_icon="📊",
    layout="wide"
)

# 타이틀
st.title("우리 팀 대시보드")
st.markdown("---")

# 환영 메시지
current_hour = datetime.now().hour
if 5 <= current_hour < 12:
    greeting = "좋은 아침이에요!"
elif 12 <= current_hour < 18:
    greeting = "좋은 오후에요!"
else:
    greeting = "좋은 저녁이에요!"

st.subheader(greeting)
st.write("우리 팀의 재미있는 데이터와 미니게임을 즐겨보세요!")

# 팀원 소개
st.markdown("---")
st.subheader("팀원 소개")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 팀원 1")
    st.write("**역할**: 메인 페이지 개발")
    st.write("**관심사**: UI/UX 디자인")
    st.write("**좋아하는 것**: 피자")
    
with col2:
    st.markdown("### 팀원 2")
    st.write("**역할**: 데이터 시각화")
    st.write("**관심사**: 데이터 분석")
    st.write("**좋아하는 것**: 차트 그리기")
    
with col3:
    st.markdown("### 팀원 3")
    st.write("**역할**: 미니게임 개발")
    st.write("**관심사**: 인터랙티브 개발")
    st.write("**좋아하는 것**: 게임 만들기")

# 빠른 시작 가이드
st.markdown("---")
st.subheader("빠른 시작")

with st.expander("사용 방법"):
    st.write("""
    1. 왼쪽 사이드바를 열어주세요
    2. 원하는 페이지를 선택하세요
    3. 각 페이지에서 다양한 기능을 체험해보세요!
    """)

# 푸터
st.markdown("---")
st.caption(f"마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
st.caption("Made with love by Team Dashboard")