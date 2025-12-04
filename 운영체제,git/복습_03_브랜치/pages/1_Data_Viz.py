# pages/1_Data_Viz.py
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="데이터 시각화", page_icon="📊", layout="wide")

st.title("데이터 시각화")
st.markdown("---")

# 팀원 데이터
team_data = {
    '이름': ['팀원 1', '팀원 2', '팀원 3'],
    '커피': [5, 3, 7],
    '코딩시간': [6, 8, 5],
    '운동시간': [1, 2, 0.5]
}

df = pd.DataFrame(team_data)

# 섹션 1: 팀원별 커피 소비량
st.subheader("팀원별 일일 커피 소비량")
col1, col2 = st.columns([2, 1])

with col1:
    fig1 = px.bar(df, x='이름', y='커피', 
                  title='하루 커피 소비량 (잔)',
                  color='커피',
                  color_continuous_scale='Blues')
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.metric("팀 평균", f"{df['커피'].mean():.1f}잔")
    st.metric("최대", f"{df['커피'].max()}잔")
    st.metric("최소", f"{df['커피'].min()}잔")

st.markdown("---")

# 섹션 2: 일일 활동 시간
st.subheader("팀원별 일일 활동 시간")

activity_df = pd.DataFrame({
    '팀원': ['팀원 1', '팀원 1', '팀원 2', '팀원 2', '팀원 3', '팀원 3'],
    '활동': ['코딩', '운동', '코딩', '운동', '코딩', '운동'],
    '시간': [6, 1, 8, 2, 5, 0.5]
})

fig2 = px.bar(activity_df, x='팀원', y='시간', color='활동',
              title='코딩 vs 운동 시간 비교',
              barmode='group')
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# 섹션 3: 인터랙티브 투표
st.subheader("오늘의 점심 메뉴 투표")

# 세션 스테이트 초기화
if 'votes' not in st.session_state:
    st.session_state.votes = {
        '한식': 0,
        '중식': 0,
        '일식': 0,
        '양식': 0
    }

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("한식", use_container_width=True):
        st.session_state.votes['한식'] += 1

with col2:
    if st.button("중식", use_container_width=True):
        st.session_state.votes['중식'] += 1

with col3:
    if st.button("일식", use_container_width=True):
        st.session_state.votes['일식'] += 1

with col4:
    if st.button("양식", use_container_width=True):
        st.session_state.votes['양식'] += 1

# 투표 결과 시각화
vote_df = pd.DataFrame({
    '메뉴': list(st.session_state.votes.keys()),
    '득표수': list(st.session_state.votes.values())
})

fig3 = px.pie(vote_df, values='득표수', names='메뉴', 
              title='현재 투표 현황')
st.plotly_chart(fig3, use_container_width=True)

# 투표 초기화 버튼
if st.button("투표 초기화"):
    st.session_state.votes = {k: 0 for k in st.session_state.votes.keys()}
    st.rerun()

# 푸터
st.markdown("---")
st.caption(f"마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}")