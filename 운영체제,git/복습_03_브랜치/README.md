# Team Dashboard Project

이 프로젝트는 3명의 팀원이 Streamlit 기반 대시보드를 협업하여 개발하는 예시 프로젝트입니다.
각 팀원은 독립적인 모듈을 담당하며, 공통 데이터(`team_data.json`)와 공용 함수(`helpers.py`)를 기반으로 기능을 구성합니다.

## 📁 프로젝트 구조

team-dashboard/
- app.py — 메인 앱 (팀원 1 담당)
- pages/
  - 1_📊_Data_Viz.py — 시각화 페이지 (팀원 2 담당)
  - 2_🎮_Games.py — 인터랙티브 페이지 (팀원 3 담당)
- data/
  - team_data.json — 공통 데이터
- utils/
  - helpers.py — 공통 함수
- requirements.txt — 필요한 패키지 목록

## 👥 팀원 역할

### 팀원 1 — 메인 애플리케이션(app.py)
- 전체 Streamlit 앱 구조 설계
- 사이드바 메뉴/레이아웃 구성
- 공통 데이터 로딩 함수 호출
- 각 페이지 연결

### 팀원 2 — 데이터 시각화 페이지(1_📊_Data_Viz.py)
- `team_data.json` 기반 데이터 분석/시각화
- 그래프(Matplotlib, Plotly 등) 구현
- 요약 통계/탭 구성

### 팀원 3 — 인터랙티브 페이지(2_🎮_Games.py)
- 간단한 게임 또는 사용자 입력 인터랙션 기능 개발
- 점수/유저 입력 처리
- 공통 함수 활용

## 🚀 실행 방법

1. 가상환경 생성(선택)
   python -m venv venv  
   source venv/bin/activate  (윈도우: venv\Scripts\activate)

2. 패키지 설치  
   pip install -r requirements.txt

3. 앱 실행  
   streamlit run app.py

## 🤝 협업 규칙(Git)

1. 각 팀원은 자신의 브랜치에서 작업한다.
2. 작업 후 단계  
   git add .  
   git commit -m "메시지"  
   git push origin 브랜치명
3. main 브랜치에는 PR(Pull Request) 로만 병합한다.

## 📌 개발 참고사항
- 모든 데이터 파일은 /data 에 저장한다.
- 공통 기능은 /utils/helpers.py 에 작성하여 import 해서 사용한다.
- 페이지 파일은 반드시 pages/숫자_이름.py 형식을 유지한다.
- Streamlit 특성상 파일명에 숫자 프리픽스를 두면 페이지 순서가 자동 정렬된다.
