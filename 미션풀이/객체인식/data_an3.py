import streamlit as st
from openai import OpenAI
import datetime
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import numpy as np

# -----------------------------------------------------------------------------
# 0. 설정 및 보조 함수
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Deep Data Analyst", page_icon="🧬", layout="wide")

# 세션 상태 초기화 (새로고침 되어도 데이터 유지)
if "messages" not in st.session_state: st.session_state.messages = []
if "analysis_result" not in st.session_state: st.session_state.analysis_result = None
if "dataset_info" not in st.session_state: st.session_state.dataset_info = None
if "current_task" not in st.session_state: st.session_state.current_task = None
if "dataset_name" not in st.session_state: st.session_state.dataset_name = ""
if "dataset_url" not in st.session_state: st.session_state.dataset_url = ""

# OpenCV 안전 임포트
try:
    import cv2
except ImportError:
    pass

# 이미지 시각화 함수들
@st.cache_data
def get_sample_image(url="https://placedog.net/500/400?r"):
    try:
        response = requests.get(url, timeout=3)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        return img
    except:
        return Image.new('RGB', (500, 400), color='gray')

def visualize_detection_sample(img):
    draw = ImageDraw.Draw(img)
    bbox = [(150, 50), (350, 250)]
    draw.rectangle(bbox, outline="red", width=4)
    try: font = ImageFont.truetype("arial.ttf", 20)
    except: font = ImageFont.load_default()
    draw.text((bbox[0][0], bbox[0][1]-25), "sample_obj: 0.99", fill="red", font=font)
    return img

def visualize_segmentation_sample(img):
    img_np = np.array(img)
    mask = np.zeros((img_np.shape[0], img_np.shape[1]), dtype=np.uint8)
    center_y, center_x = img_np.shape[0] // 2, img_np.shape[1] // 2
    y, x = np.ogrid[:img_np.shape[0], :img_np.shape[1]]
    mask[(x - center_x)**2 + (y - center_y)**2 <= 100**2] = 1
    
    color_mask = np.zeros_like(img_np)
    color_mask[mask == 1] = [0, 0, 255] # Blue
    
    if 'cv2' in globals():
        return Image.fromarray(cv2.addWeighted(img_np, 1, color_mask, 0.5, 0))
    else:
        return img # Fallback

# 분석 함수
def run_specific_analysis(key, data_name, data_url, task):
    client = OpenAI(api_key=key)
    system_prompt = f"""
    당신은 컴퓨터 비전 데이터셋 전문가입니다.
    사용자가 제공한 데이터셋 이름('{data_name}')과 URL('{data_url}')을 바탕으로 분석하세요.
    
    지시사항:
    1. **일반론 금지**: 교과서적인 설명 대신 구체적인 사실(Fact) 위주로 서술하세요.
    2. **구조 파악**: 해당 URL의 데이터셋이 어떤 폴더 구조와 파일 포맷(XML, JSON, PNG Mask 등)을 쓰는지 명시하세요.
    3. **Task 특화 이슈**: {task} 수행 시 이 데이터셋만의 고유한 문제점과 해결책을 제시하세요.
    """
    with st.spinner(f"🕵️‍♂️ {data_name} 심층 분석 중..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": system_prompt}, 
                      {"role": "user", "content": f"데이터셋 스펙과 {task} 수행 시 주의할 점(Pitfalls) 분석해줘."}],
            temperature=0.3
        )
        return response.choices[0].message.content

# -----------------------------------------------------------------------------
# 1. 사이드바 (설정 및 실행)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ 분석 설정")
    api_key = st.text_input("OpenAI API Key", type="password")
    
    st.divider()
    
    # 입력값 받기
    in_name = st.text_input("데이터셋 이름", "Oxford-IIIT Pet Dataset")
    in_url = st.text_input("데이터셋 링크 (URL)", placeholder="예: https://www.robots.ox.ac.uk/~vgg/data/pets/")
    in_task = st.selectbox("수행할 태스크", ["객체인식 (Object Detection)", "세그멘테이션 (Segmentation)", "이미지 분류", "GAN"])
    
    # 실행 버튼
    if st.button("🚀 심층 분석 시작", type="primary"):
        if not api_key:
            st.error("API Key를 입력해주세요.")
        else:
            # 상태 저장
            st.session_state.dataset_name = in_name
            st.session_state.dataset_url = in_url
            st.session_state.current_task = in_task
            st.session_state.messages = [] # 대화 초기화
            
            # 분석 실행 및 결과 저장
            result = run_specific_analysis(api_key, in_name, in_url, in_task)
            st.session_state.analysis_result = result
            st.session_state.messages.append({"role": "assistant", "content": result}) # 초기 분석을 대화 기록에 추가

    st.divider()
    
    # 다운로드 버튼 (분석 결과가 있을 때만 활성화)
    if st.session_state.analysis_result:
        report_txt = f"# 📊 데이터 분석 리포트\n\n**Dataset:** {st.session_state.dataset_name}\n**Task:** {st.session_state.current_task}\n**URL:** {st.session_state.dataset_url}\n\n---\n\n{st.session_state.analysis_result}\n\n---\n\n## 질의응답 기록\n"
        for msg in st.session_state.messages:
            if msg['role'] == 'user': report_txt += f"\n**Q:** {msg['content']}\n"
            if msg['role'] == 'assistant' and msg['content'] != st.session_state.analysis_result: report_txt += f"\n**A:** {msg['content']}\n"
            
        st.download_button("📄 통합 리포트 다운로드 (.md)", report_txt, file_name="analysis_report.md")

# -----------------------------------------------------------------------------
# 2. 메인 화면 구성
# -----------------------------------------------------------------------------
st.title("🧬 Deep Data Analyst")

# 분석 결과가 메모리에 있을 경우에만 화면 표시 (새로고침 되어도 유지됨)
if st.session_state.analysis_result:
    
    st.info(f"✅ 분석 대상: **{st.session_state.dataset_name}** | 태스크: **{st.session_state.current_task}**")

    # 탭 구성: 분석 / 시각화 / 채팅
    tab1, tab2, tab3 = st.tabs(["📊 심층 분석 리포트", "👀 샘플 시각화", "💬 AI 데이터 컨설턴트 (Q&A)"])

    # --- TAB 1: 심층 분석 (읽기 전용) ---
    with tab1:
        st.markdown(st.session_state.analysis_result)
        st.warning("⚠️ 이 리포트는 AI 분석 결과입니다. 실제 데이터와 일부 차이가 있을 수 있습니다.")

    # --- TAB 2: 시각화 ---
    with tab2:
        st.subheader("데이터 포맷 시각화 (Simulation)")
        col_img, col_desc = st.columns([1, 1])
        base_img = get_sample_image()
        
        with col_img:
            if "객체인식" in st.session_state.current_task:
                st.image(visualize_detection_sample(base_img.copy()), caption="Bounding Box 예상")
            elif "세그멘테이션" in st.session_state.current_task:
                st.image(visualize_segmentation_sample(base_img.copy()), caption="Segmentation Mask 예상")
            else:
                st.image(base_img, caption="원본 이미지 (시각적 어노테이션 없음)")
                
        with col_desc:
            st.markdown(f"""
            **{st.session_state.current_task}** 데이터셋의 예상 형태입니다.
            실제 데이터를 다운로드하지 않고, 포맷을 유추하여 시각화했습니다.
            - **객체인식**: XML/TXT 좌표를 이미지에 사각형으로 매핑
            - **세그멘테이션**: PNG 마스크 파일을 이미지에 오버레이
            """)

    # --- TAB 3: 질의응답 (Q&A) ---
    with tab3:
        st.subheader("💬 데이터 전문 Q&A")
        st.caption("분석 리포트를 바탕으로 궁금한 점을 물어보세요. (예: '이거 전처리하는 파이썬 코드 짜줘')")
        
        # 채팅 히스토리 출력 (컨테이너 사용으로 스크롤 관리)
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.messages:
                # 초기 긴 분석글은 채팅창에서 제외하고 싶으면 아래 if문 사용 (여기선 포함함)
                if message['role'] != "system":
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

        # 채팅 입력창 (탭 내부 하단에 고정)
        if prompt := st.chat_input("질문을 입력하세요..."):
            if not api_key:
                st.error("API Key가 필요합니다.")
            else:
                # 1. 사용자 메시지 추가
                st.session_state.messages.append({"role": "user", "content": prompt})
                with chat_container:
                    with st.chat_message("user"):
                        st.markdown(prompt)

                # 2. AI 응답 생성
                client = OpenAI(api_key=api_key)
                
                # 대화 컨텍스트 구성
                context_msgs = [
                    {"role": "system", "content": f"당신은 {st.session_state.dataset_name} 데이터셋 전문 컨설턴트입니다. 코드 작성, 폴더 구조 설명 등 실무적인 답변을 제공하세요."}
                ] + st.session_state.messages

                with chat_container:
                    with st.chat_message("assistant"):
                        stream = client.chat.completions.create(
                            model="gpt-4o",
                            messages=context_msgs,
                            stream=True
                        )
                        response = st.write_stream(stream)
                
                # 3. 응답 저장
                st.session_state.messages.append({"role": "assistant", "content": response})

else:
    # 초기 화면
    st.info("👈 왼쪽 사이드바에서 데이터셋 정보를 입력하고 '분석 시작'을 눌러주세요.")