# pages/2_Games.py
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="미니게임", page_icon="🎮", layout="wide")

st.title("미니게임")
st.markdown("---")

# 게임 선택 탭
tab1, tab2, tab3 = st.tabs(["팀원 퀴즈", "점심 메뉴 룰렛", "오늘의 운세"])

# 탭 1: 팀원 퀴즈
with tab1:
    st.subheader("팀원 맞추기 퀴즈")
    st.write("힌트를 보고 누구인지 맞춰보세요!")
    
    # 퀴즈 데이터
    quiz_data = [
        {
            "힌트": "UI/UX 디자인에 관심이 많고 피자를 좋아합니다",
            "정답": "팀원 1",
            "선택지": ["팀원 1", "팀원 2", "팀원 3"]
        },
        {
            "힌트": "데이터 분석을 좋아하고 하루에 커피를 가장 적게 마십니다",
            "정답": "팀원 2",
            "선택지": ["팀원 1", "팀원 2", "팀원 3"]
        },
        {
            "힌트": "게임 만들기를 좋아하고 커피를 가장 많이 마십니다",
            "정답": "팀원 3",
            "선택지": ["팀원 1", "팀원 2", "팀원 3"]
        }
    ]
    
    # 세션 스테이트 초기화
    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
    
    if st.session_state.quiz_index < len(quiz_data):
        current_quiz = quiz_data[st.session_state.quiz_index]
        
        st.info(f"문제 {st.session_state.quiz_index + 1}: {current_quiz['힌트']}")
        
        answer = st.radio("누구일까요?", current_quiz['선택지'], key=f"quiz_{st.session_state.quiz_index}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("정답 확인", disabled=st.session_state.answered):
                st.session_state.answered = True
                if answer == current_quiz['정답']:
                    st.success("정답입니다!")
                    st.session_state.score += 1
                else:
                    st.error(f"틀렸습니다. 정답은 {current_quiz['정답']}입니다.")
        
        with col2:
            if st.button("다음 문제", disabled=not st.session_state.answered):
                st.session_state.quiz_index += 1
                st.session_state.answered = False
                st.rerun()
    else:
        st.success(f"퀴즈 완료! 점수: {st.session_state.score}/{len(quiz_data)}")
        if st.button("다시 시작"):
            st.session_state.quiz_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.rerun()

# 탭 2: 점심 메뉴 룰렛
with tab2:
    st.subheader("점심 메뉴 추천 룰렛")
    st.write("오늘 점심 메뉴를 정하지 못했나요? 룰렛을 돌려보세요!")
    
    menus = [
        "한식 - 김치찌개",
        "한식 - 된장찌개",
        "중식 - 짜장면",
        "중식 - 짬뽕",
        "일식 - 초밥",
        "일식 - 라멘",
        "양식 - 파스타",
        "양식 - 스테이크",
        "분식 - 떡볶이",
        "패스트푸드 - 햄버거"
    ]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("룰렛 돌리기", use_container_width=True):
            selected_menu = random.choice(menus)
            st.session_state.selected_menu = selected_menu
    
    with col2:
        if st.button("다시 돌리기", use_container_width=True):
            selected_menu = random.choice(menus)
            st.session_state.selected_menu = selected_menu
    
    if 'selected_menu' in st.session_state:
        st.success(f"오늘의 메뉴는: **{st.session_state.selected_menu}**")
        st.balloons()

# 탭 3: 오늘의 운세
with tab3:
    st.subheader("오늘의 팀원 운세")
    st.write("오늘 우리 팀의 운세를 확인해보세요!")
    
    fortunes = [
        "오늘은 코드가 술술 풀리는 날입니다!",
        "예상치 못한 버그를 발견할 수 있습니다. 주의하세요.",
        "동료와의 협업이 순조로운 날입니다.",
        "커피 한 잔이 큰 힘이 되는 날입니다.",
        "오늘은 휴식이 필요한 날입니다.",
        "새로운 아이디어가 떠오르는 날입니다!",
        "집중력이 최고조에 달하는 날입니다.",
        "점심 메뉴 선택에 고민이 많은 날입니다."
    ]
    
    lucky_numbers = [1, 3, 7, 9, 13, 21, 42, 77, 99]
    
    team_member = st.selectbox("팀원을 선택하세요", ["팀원 1", "팀원 2", "팀원 3"])
    
    if st.button("운세 보기", use_container_width=True):
        # 팀원 이름을 시드로 사용하여 하루 동안 같은 운세가 나오도록
        today = datetime.now().strftime("%Y-%m-%d")
        seed = hash(team_member + today)
        random.seed(seed)
        
        fortune = random.choice(fortunes)
        lucky_number = random.choice(lucky_numbers)
        luck_score = random.randint(60, 100)
        
        st.markdown(f"### {team_member}의 오늘의 운세")
        st.info(fortune)
        st.write(f"**행운의 숫자**: {lucky_number}")
        st.write(f"**운세 점수**: {luck_score}점")
        
        # 운세 점수에 따른 프로그레스 바
        st.progress(luck_score / 100)
        
        if luck_score >= 90:
            st.success("최고의 하루가 될 것입니다!")
        elif luck_score >= 75:
            st.info("좋은 하루가 될 것입니다!")
        else:
            st.warning("무난한 하루가 될 것입니다.")

# 푸터
st.markdown("---")
st.caption(f"마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}")