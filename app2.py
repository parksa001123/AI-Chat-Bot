from openai import OpenAI
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# -----------------------------------
# 기본 설정
# -----------------------------------

st.set_page_config(
    page_title="KW Student Adventure",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------------
# OpenAI API
# -----------------------------------

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# -----------------------------------
# 사용자 계정
# -----------------------------------

users = {
    "student": {
        "password": "1234",
        "role": "학생"
    },
    "professor": {
        "password": "1234",
        "role": "교수자"
    }
}

# -----------------------------------
# 세션
# -----------------------------------

if "login" not in st.session_state:
    st.session_state.login = False

if "role" not in st.session_state:
    st.session_state.role = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# 로그인 화면
# -----------------------------------

if not st.session_state.login:

    st.markdown("""
    # 🎓 KW Student Adventure
    
    ### 학생성공 기반 AI 비교과 플랫폼
    
    진로 · 학습 · 정서 · 대학생활  
    맞춤형 성장 지원 시스템
    """)

    st.image(
        "https://images.unsplash.com/photo-1523050854058-8df90110c9f1",
        use_container_width=True
    )

    id_input = st.text_input("아이디")
    pw_input = st.text_input("비밀번호", type="password")

    if st.button("로그인"):

        if id_input in users:

            if users[id_input]["password"] == pw_input:

                st.session_state.login = True
                st.session_state.role = users[id_input]["role"]

                st.success("로그인 성공")
                st.rerun()

            else:
                st.error("비밀번호 오류")

        else:
            st.error("아이디가 존재하지 않습니다")

    st.stop()

# -----------------------------------
# 사이드바
# -----------------------------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=120
    )

    st.markdown(f"""
    ### 👋 {st.session_state.role} 로그인
    """)

    if st.session_state.role == "학생":

        selected = option_menu(
            menu_title="메뉴",
            options=[
                "홈",
                "AI 추천",
                "프로그램 탐색",
                "퀘스트",
                "성장이력",
                "AI 코치"
            ],
            icons=[
                "house",
                "robot",
                "search",
                "trophy",
                "graph-up",
                "chat-dots"
            ],
            default_index=0
        )

    else:

        selected = option_menu(
            menu_title="교수자 메뉴",
            options=[
                "교수자 대시보드",
                "학생 분석",
                "프로그램 관리",
                "AI 추천 통계"
            ],
            icons=[
                "bar-chart",
                "people",
                "gear",
                "robot"
            ],
            default_index=0
        )

# -----------------------------------
# 홈
# -----------------------------------

if selected == "홈":

    st.title("🎓 KW Student Adventure")

    col1, col2 = st.columns([1,2])

    with col1:

        st.markdown("""
        ## 홍길동
        
        AI융합학부
        
        ### Explorer Lv.2
        """)

        st.progress(0.65)

        st.markdown("EXP 1260 / 2000")

    with col2:

        categories = [
            "디지털문해력",
            "상호작용능력",
            "윤리적시민의식",
            "자기주도성",
            "확장적사고력",
            "대학생활지원"
        ]

        values = [85,72,68,80,75,70]

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0,100]
                )),
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("🔥 추천 퀘스트")

    q1, q2, q3 = st.columns(3)

    q1.info("""
    ### AI Starter Quest
    
    생성형 AI 특강 참여
    
    EXP +50
    """)

    q2.info("""
    ### Career Builder
    
    진로설계 워크숍
    
    EXP +100
    """)

    q3.info("""
    ### Campus Connect
    
    대학생활 적응 캠프
    
    EXP +40
    """)

# -----------------------------------
# AI 추천
# -----------------------------------

elif selected == "AI 추천":

    st.title("🤖 AI 맞춤 추천")

    career = st.slider("진로불안",1,5,4)
    digital = st.slider("디지털문해력",1,5,2)
    leadership = st.slider("자기주도성",1,5,2)

    recommendations = []

    if career >= 4:
        recommendations.append("🎯 진로설계 워크숍")

    if digital <= 2:
        recommendations.append("💻 AI 기초 특강")

    if leadership <= 2:
        recommendations.append("📚 자기주도 학습코칭")

    st.markdown("---")

    for item in recommendations:
        st.success(item)

    st.info("""
    AI 분석 결과:
    
    진로 탐색과 자기주도 학습 역량 향상이 필요합니다.
    단계적 성장 프로그램 참여를 추천합니다.
    """)

# -----------------------------------
# 프로그램 탐색
# -----------------------------------

elif selected == "프로그램 탐색":

    st.title("📚 비교과 프로그램 탐색")

    programs = pd.DataFrame({

        "프로그램":[
            "AI 노마드 특강",
            "진로설계 워크숍",
            "창업 아이디어 챌린지",
            "대학생활 적응 캠프"
        ],

        "영역":[
            "디지털",
            "진로",
            "창업",
            "대학생활"
        ],

        "핵심역량":[
            "디지털문해력",
            "자기주도성",
            "확장적사고력",
            "대학생활지원"
        ],

        "EXP":[50,30,100,20]
    })

    st.dataframe(programs, use_container_width=True)

# -----------------------------------
# 퀘스트
# -----------------------------------

elif selected == "퀘스트":

    st.title("🏆 성장 퀘스트")

    st.progress(0.5)

    st.success("""
    AI Starter Quest
    
    생성형 AI 특강 참여
    
    진행도 1/2
    """)

    st.markdown("---")

    st.progress(1.0)

    st.info("""
    Campus Connect
    
    대학생활 적응 프로그램
    
    완료
    """)

# -----------------------------------
# 성장이력
# -----------------------------------

elif selected == "성장이력":

    st.title("📈 성장 Transcript")

    transcript = pd.DataFrame({

        "프로그램":[
            "AI 특강",
            "진로 워크숍",
            "창업 챌린지"
        ],

        "핵심역량":[
            "디지털문해력",
            "자기주도성",
            "확장적사고력"
        ],

        "EXP":[50,30,100]
    })

    st.dataframe(transcript, use_container_width=True)

# -----------------------------------
# AI 코치
# -----------------------------------

elif selected == "AI 코치":

    st.title("🤖 KW 학생성공 AI 코치")

    st.markdown("""
    진로 · 학습 · 정서 · 대학생활 기반
    
    실시간 AI 상담 및 비교과 추천 시스템
    """)

    system_prompt = """
    당신은 경운대학교 학생성공 AI 코치입니다.

    학생의:
    - 진로
    - 학습
    - 정서
    - 대학생활
    - 창업
    - 핵심역량

    을 분석하여 비교과 프로그램을 추천하세요.

    답변 형식:
    1. 학생 상태 분석
    2. 추천 프로그램
    3. 추천 이유
    4. 성장 방향 제안
    """

    if len(st.session_state.messages) == 0:

        st.session_state.messages.append({
            "role":"system",
            "content":system_prompt
        })

    for message in st.session_state.messages[1:]:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("현재 고민이나 필요한 지원을 입력하세요"):

        st.session_state.messages.append({
            "role":"user",
            "content":prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages,
                stream=True
            )

            response = st.write_stream(stream)

        st.session_state.messages.append({
            "role":"assistant",
            "content":response
        })

# -----------------------------------
# 교수자 대시보드
# -----------------------------------

elif selected == "교수자 대시보드":

    st.title("🧑‍🏫 교수자 Dashboard")

    c1,c2,c3 = st.columns(3)

    c1.metric("운영 프로그램","12개")
    c2.metric("참여 학생","428명")
    c3.metric("평균 만족도","4.7")

    st.bar_chart(pd.DataFrame({
        "역량":[
            "디지털문해력",
            "상호작용능력",
            "자기주도성"
        ],
        "수준":[85,72,80]
    }).set_index("역량"))

# -----------------------------------
# 학생 분석
# -----------------------------------

elif selected == "학생 분석":

    st.title("📊 위험학생 분석")

    risk = pd.DataFrame({

        "학생":[
            "홍길동",
            "김민수",
            "이서연"
        ],

        "위험도":[
            "중간",
            "높음",
            "낮음"
        ],

        "추천지원":[
            "진로상담",
            "정서지원",
            "창업멘토링"
        ]
    })

    st.dataframe(risk, use_container_width=True)

# -----------------------------------
# 프로그램 관리
# -----------------------------------

elif selected == "프로그램 관리":

    st.title("⚙️ 프로그램 관리")

    st.text_input("프로그램명")

    st.selectbox(
        "영역",
        ["진로","학습","창업","정서","대학생활"]
    )

    if st.button("등록"):
        st.success("등록 완료")

# -----------------------------------
# AI 추천 통계
# -----------------------------------

elif selected == "AI 추천 통계":

    st.title("🤖 AI 추천 통계")

    st.metric("총 추천 횟수","1240")

    chart = pd.DataFrame({
        "영역":["진로","학습","창업"],
        "추천수":[420,380,210]
    })

    st.bar_chart(chart.set_index("영역"))