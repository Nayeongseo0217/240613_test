import openai
import streamlit as st

st.title("AUTO CONNECT CHAT BOT")

# 안내 문구 추가
st.markdown("""
안녕하세요. 환영합니다!<br><br>
자동차 종합 모빌리티 플랫폼 오토커넥트입니다!<br><br>
나만의 모빌리티를 찾기 위한 여정, 너무 어려우시죠?<br>
오토커넥트 나만의 AI파트너, "AUTO CONNECT CHAT BOT"이 도와드리겠습니다^^<br><br>
*언제든지 더 자세한 상담을 원하신다면 지금 바로 전화해주세요! 상담가능 시간(00:00~23:59)<br>
-> 전화 상담 : 010 - XXXX - XXXX
""", unsafe_allow_html=True)

# 구분선 추가
st.markdown("<hr>", unsafe_allow_html=True)

# 맨 처음에 버튼 5개 생성
if "button_state" not in st.session_state:
    st.session_state.button_state = "main"

# 버튼 생성 관리
def main_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 컨설팅 부서를 선택해주세요!</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("신차구매 컨설팅"):
        st.session_state.button_state = "신차구매 컨설팅"
    if st.button("중고차구매 컨설팅"):
        st.session_state.button_state = "중고차구매 컨설팅"
    if st.button("리스렌트 승계 컨설팅"):
        st.session_state.button_state = "리스렌트 승계 컨설팅"
    if st.button("A/S 사후관리 컨설팅"):
        st.session_state.button_state = "사후관리 컨설팅"
    if st.button("법인 전문 컨설팅 의뢰"):
        st.session_state.button_state = "법인 전문 컨설팅 의뢰"

def 신차구매_컨설팅_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 종류에 관심이 있으신가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("국산차"):
        st.session_state.button_state = "국산차"
    if st.button("수입차"):
        st.session_state.button_state = "수입차"
    if st.button("최신 인기차량 추천받기"):
        st.session_state.button_state = "최신 인기차량 추천받기"
    if st.button("나만의 모빌리티 선택하기"):
        st.session_state.button_state = "나만의 모빌리티 선택하기"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "main"

def 중고차구매_컨설팅_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 종류에 관심이 있으신가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>중고차구매 컨설팅</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "main"

def 리스렌트_승계_컨설팅_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 종류에 관심이 있으신가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>리스렌트 승계 컨설팅</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "main"

def 사후관리_컨설팅_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 종류에 관심이 있으신가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>A/S 사후관리 컨설팅</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "main"

def 법인_전문_컨설팅_의뢰_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 종류에 관심이 있으신가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>법인 전문 컨설팅 의뢰</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "main"

def 국산차_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 제조사는 어디인가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("현대"):
        st.session_state.button_state = "현대"
    if st.button("제네시스"):
        st.session_state.button_state = "제네시스"
    if st.button("기아"):
        st.session_state.button_state = "기아"
    if st.button("쉐보레"):
        st.session_state.button_state = "쉐보레"
    if st.button("KG 모빌리티"):
        st.session_state.button_state = "KG 모빌리티"
    if st.button("르노"):
        st.session_state.button_state = "르노"
    if st.button("디피코"):
        st.session_state.button_state = "디피코"
    if st.button("스마트 EV"):
        st.session_state.button_state = "스마트 EV"
    if st.button("마이브"):
        st.session_state.button_state = "마이브"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "신차구매 컨설팅"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 수입차_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 제조사는 어디인가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("유럽"):
        st.session_state.button_state = "유럽"
    if st.button("미국"):
        st.session_state.button_state = "미국"
    if st.button("일본"):
        st.session_state.button_state = "일본"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "신차구매 컨설팅"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 최신_인기차량_추천받기_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 최신 인기차량을 추천해드리겠습니다!</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 최신 인기차량 추천받기</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 나만의_모빌리티_선택하기_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 구체적인 정보를 입력해주세요!</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 나만의 모빌리티 선택하기</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 현대_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("[경차] 캐스퍼"):
        st.session_state.button_state = "캐스퍼"
    if st.button("[준중형] 더 뉴 아반떼(CN7 F/L)"):
        #st.session_state.button_state = "더 뉴 아반떼(CN7 F/L)"
        st.session_state.button_state = "main"
    if st.button("[준중형] 더 뉴 아반떼N(CN7 F/L)"):
        #st.session_state.button_state = "더 뉴 아반떼N(CN7 F/L)"
        st.session_state.button_state = "main"
    if st.button("[준중형] 더 뉴 아반떼HEV(CN7 F/L)"):
        #st.session_state.button_state = "더 뉴 아반떼HEV(CN7 F/L)"
        st.session_state.button_state = "main"
    if st.button("[중형] 쏘나타 디 엣지(DN8 F/L)"):
        #st.session_state.button_state = "쏘나타 디 엣지(DN8 F/L)"
        st.session_state.button_state = "main"
    if st.button("[중형] 쏘나타 디 엣지HEV(DN8 F/L)"):
        #st.session_state.button_state = "쏘나타 디 엣지HEV(DN8 F/L)"
        st.session_state.button_state = "main"
    if st.button("[중형] 아이오닉6"):
        #st.session_state.button_state = "아이오닉6"
        st.session_state.button_state = "main"
    if st.button("[준대형] 디 올-뉴 그랜저(GN7)"):
        #st.session_state.button_state = "디 올-뉴 그랜저(GN7)"
        st.session_state.button_state = "main"
    if st.button("[준대형] 디 올-뉴 그랜저HEV(GN7)"):
        #st.session_state.button_state = "디 올-뉴 그랜저HEV(GN7)"
        st.session_state.button_state = "main"
    if st.button("[소형SUV] 베뉴"):
        #st.session_state.button_state = "베뉴"
        st.session_state.button_state = "main"
    if st.button("[소형SUV] 디 올 뉴 코나(SX2)"):
        #st.session_state.button_state = "디 올 뉴 코나(SX2)"
        st.session_state.button_state = "main"
    if st.button("[소형SUV] 디 올 뉴 코나HEV(SX2)"):
        #st.session_state.button_state = "디 올 뉴 코나HEV(SX2)"
        st.session_state.button_state = "main"
    if st.button("[소형SUV] 디 올 뉴 코나EV(SX2)"):
        #st.session_state.button_state = "디 올 뉴 코나EV(SX2)"
        st.session_state.button_state = "main"
    if st.button("[준중형SUV] 넥쏘"):
        #st.session_state.button_state = "넥쏘"
        st.session_state.button_state = "main"
    if st.button("[준중형SUV] 더 뉴 투싼(NX4 F/L)"):
        #st.session_state.button_state = "더 뉴 투싼(NX4 F/L)"
        st.session_state.button_state = "main"
    if st.button("[준중형SUV] 더 뉴 투싼HEV(NX4 F/L)"):
        #st.session_state.button_state = "더 뉴 투싼HEV(NX4 F/L)"
        st.session_state.button_state = "main"
    if st.button("[중형SUV] 디 올-뉴 산타페(MX5)"):
        #st.session_state.button_state = "디 올-뉴 산타페(MX5)"
        st.session_state.button_state = "main"
    if st.button("[중형SUV] 디 올-뉴 산타페HEV(MX5)"):
        #st.session_state.button_state = "디 올-뉴 산타페HEV(MX5)"
        st.session_state.button_state = "main"
    if st.button("[중형SUV] 더 뉴 아이오닉5"):
        #st.session_state.button_state = "더 뉴 아이오닉5"
        st.session_state.button_state = "main"
    if st.button("[중형SUV] 아이오닉5"):
        #st.session_state.button_state = "아이오닉5"
        st.session_state.button_state = "main"
    if st.button("[중형SUV] 아이오닉5N"):
        #st.session_state.button_state = "아이오닉5N"
        st.session_state.button_state = "main"
    if st.button("[대형SUV] 더 뉴 팰리세이드"):
        #st.session_state.button_state = "더 뉴 팰리세이드"
        st.session_state.button_state = "main"
    if st.button("[RV/MPV] 스타리아"):
        #st.session_state.button_state = "스타리아"
        st.session_state.button_state = "main"
    if st.button("[RV/MPV] 스타리아HEV"):
        #st.session_state.button_state = "스타리아HEV"
        st.session_state.button_state = "main"
    if st.button("[RV/MPV] 스타리아 아클란"):
        #st.session_state.button_state = "스타리아 아클란"
        st.session_state.button_state = "main"
    if st.button("[RV/MPV] 스타리아 아클란S"):
        #st.session_state.button_state = "스타리아 아클란S"
        st.session_state.button_state = "main"
    if st.button("[상용] ST1"):
        #st.session_state.button_state = "ST1"
        st.session_state.button_state = "main"
    if st.button("[상용] 더 뉴 포터II"):
        #st.session_state.button_state = "더 뉴 포터II"
        st.session_state.button_state = "main"
    if st.button("[상용] 더 뉴 포터II 특장차"):
        #st.session_state.button_state = "더 뉴 포터II 특장차"
        st.session_state.button_state = "main"
    if st.button("[상용] 포터II EV"):
        #st.session_state.button_state = "포터II EV"
        st.session_state.button_state = "main"
    if st.button("[상용] 포터II EV 특장차"):
        #st.session_state.button_state = "포터II EV 특장차"
        st.session_state.button_state = "main"
    if st.button("[상용] 올 뉴마이티"):
        #st.session_state.button_state = "올 뉴마이티"
        st.session_state.button_state = "main"
    if st.button("[상용] 쏠라티"):
        #st.session_state.button_state = "쏠라티"
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 제네시스_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 제네시스</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("[준대형] G80(RG3 F/L)"):
        st.session_state.button_state = "G80(RG3 F/L)"
    if st.button("[준대형] G80(RG3)"):
        st.session_state.button_state = "G80(RG3)"
    if st.button("[준대형] e-G80(RG3)"):
        st.session_state.button_state = "e-G80(RG3)"
    if st.button("[대형] 신형 G90(RS4)"):
        st.session_state.button_state = "신형 G90(RS4)"
    if st.button("[중형SUV] GV70(JK)"):
        st.session_state.button_state = "GV70(JK)"
    if st.button("[대형SUV] GV80(JK)"):
        st.session_state.button_state = "GV80(JK)"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 기아_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 기아</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("[경차] 레이 EV(PE)"):
        st.session_state.button_state = "레이 EV(PE)"
    if st.button("[중형SUV] 더 뉴 쏘렌토(MQ4 F/L)"):
        st.session_state.button_state = "더 뉴 쏘렌토(MQ4 F/L)"
    if st.button("[중형] 더 뉴 K5 EV(DL3 F/L)"):
        st.session_state.button_state = "레이 EV(PE)"
    if st.button("[RV/MPV] 카니발 LM"):
        st.session_state.button_state = "카니발 LM"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 쉐보레_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 쉐보레</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def KG_모빌리티_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > KG 모빌리티</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 르노_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 르노</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 디피코_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 디피코</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 스마트_EV_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 스마트 EV</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 마이브_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 마이브</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "국산차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 벤츠_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 벤츠</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("[중형] The New C-Class(W206)"):
        st.session_state.button_state = "The New C-Class(W206)"
    if st.button("[준대형] The New E-Class(W214)"):
        st.session_state.button_state = "The New E-Class(W214)"
    if st.button("[대형] S-Class(W223)"):
        st.session_state.button_state = "S-Class(W223)"
    if st.button("[대형SUV] The New GLE-Class(2세대 F/L)"):
        st.session_state.button_state = "The New GLE-Class(2세대 F/L)"
    if st.button("[대형SUV] The New GLS-Class(2세대 F/L)"):
        st.session_state.button_state = "The New GLS-Class(2세대 F/L)"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def BMW_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > BMW</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("[준대형] 5 Series(G60)"):
        st.session_state.button_state = "5 Series(G60)"
    if st.button("[대형] 7 Series(G70)"):
        st.session_state.button_state = "7 Series(G70)"
    if st.button("[대형SUV] The New X5(4세대 F/L)"):
        st.session_state.button_state = "The New X5(4세대 F/L)"
    if st.button("[대형SUV] The New X7(1세대 F/L)"):
        st.session_state.button_state = "The New X7(1세대 F/L)"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 아우디_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 아우디</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 폭스바겐_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 폭스바겐</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 미니_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 미니</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 볼보_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 볼보</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 폴스타_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 폴스타</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 랜드로버_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 랜드로버</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 포르쉐_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 포르쉐</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 람보르기니_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 람보르기니</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 벤틀리_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 벤틀리</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 맥라렌_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 맥라렌</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 페라리_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 페라리</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 애스턴마틴_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 애스턴마틴</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 로터스_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 로터스</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 마세라티_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 마세라티</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 롤스로이스_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 롤스로이스</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 푸조_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 푸조</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 이네오스_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽 > 이네오스</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 포드_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 미국 > 포드</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 링컨_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 미국 > 링컨</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 지프_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 미국 > 지프</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def GMC_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 미국 > GMC</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐딜락_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 미국 > 캐딜락</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 테슬라_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 미국 > 테슬라</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 토요타_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 일본 > 토요타</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 렉서스_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 일본 > 렉서스</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 혼다_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 어떤 차종을 원하시나요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 일본 > 혼다</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("미구현"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_stete = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"


def 캐스퍼_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 세부옵션을 선택해주세요!</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("2023년형 가솔린1.0 2WD"):
        st.session_state.button_state = "캐스퍼 세부모델 1"
    if st.button("2023년형 가솔린1.0 2WD밴"):
        st.session_state.button_state = "캐스퍼 세부모델 2"
    if st.button("2023년형 가솔린1.0터보 액티브 I 2WD"):
        st.session_state.button_state = "캐스퍼 세부모델 3"
    if st.button("2023년형 가솔린1.0터보 액티브 II 2WD"):
        st.session_state.button_state = "캐스퍼 세부모델 4"
    if st.button("2023년형 가솔린1.0터보 액티브 I 2WD밴"):
        st.session_state.button_state = "캐스퍼 세부모델 5"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "현대"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_1_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 세부옵션을 선택해주세요!</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0 2WD</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("스마트(자동)"):
        st.session_state.button_state = "세1 스마트(자동)"
    if st.button("디 에센셜 라이트(자동)"):
        st.session_state.button_state = "세1 디 에센셜 라이트(자동)"
    if st.button("디 에센셜(자동)"):
        st.session_state.button_state = "세1 디 에센셜(자동)"
    if st.button("인스퍼레이션(자동)"):
        st.session_state.button_state = "세1 인스퍼레이션(자동)"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_1_스마트_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 차의 외관 색상은 어떤 색이 좋을까요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0 2WD > 스마트(자동)</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("NES-언블리치드 아이보리"):
        st.session_state.button_state = "main"
    if st.button("R4G-티탄 그레이 메탈릭"):
        st.session_state.button_state = "main"
    if st.button("SAW-아틀라스 화이트"):
        st.session_state.button_state = "main"
    if st.button("SOP-소울트로닉 오렌지 펄"):
        st.session_state.button_state = "main"
    if st.button("TKS-톰보이 카키"):
        st.session_state.button_state = "main"
    if st.button("YP5-인텐스블루 펄"):
        st.session_state.button_state = "main"
    if st.button("TKM-비자림 카키 매트"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼 세부모델 1"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_1_디_에센셜_라이트_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 차의 외관 색상은 어떤 색이 좋을까요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0 2WD > 디 에센셜 라이트(자동)</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("NES-언블리치드 아이보리"):
        st.session_state.button_state = "main"
    if st.button("R4G-티탄 그레이 메탈릭"):
        st.session_state.button_state = "main"
    if st.button("SAW-아틀라스 화이트"):
        st.session_state.button_state = "main"
    if st.button("SOP-소울트로닉 오렌지 펄"):
        st.session_state.button_state = "main"
    if st.button("TKS-톰보이 카키"):
        st.session_state.button_state = "main"
    if st.button("YP5-인텐스블루 펄"):
        st.session_state.button_state = "main"
    if st.button("TKM-비자림 카키 매트"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼 세부모델 1"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_1_디_에센셜_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 차의 외관 색상은 어떤 색이 좋을까요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0 2WD > 디 에센셜(자동)</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("NES-언블리치드 아이보리"):
        st.session_state.button_state = "main"
    if st.button("R4G-티탄 그레이 메탈릭"):
        st.session_state.button_state = "main"
    if st.button("SAW-아틀라스 화이트"):
        st.session_state.button_state = "main"
    if st.button("SOP-소울트로닉 오렌지 펄"):
        st.session_state.button_state = "main"
    if st.button("TKS-톰보이 카키"):
        st.session_state.button_state = "main"
    if st.button("YP5-인텐스블루 펄"):
        st.session_state.button_state = "main"
    if st.button("TKM-비자림 카키 매트"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼 세부모델 1"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_1_인스퍼레이션_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 차의 외관 색상은 어떤 색이 좋을까요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0 2WD > 인스퍼레이션(자동)</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("NES-언블리치드 아이보리"):
        st.session_state.button_state = "main"
    if st.button("R4G-티탄 그레이 메탈릭"):
        st.session_state.button_state = "main"
    if st.button("SAW-아틀라스 화이트"):
        st.session_state.button_state = "main"
    if st.button("SOP-소울트로닉 오렌지 펄"):
        st.session_state.button_state = "main"
    if st.button("TKS-톰보이 카키"):
        st.session_state.button_state = "main"
    if st.button("YP5-인텐스블루 펄"):
        st.session_state.button_state = "main"
    if st.button("TKM-비자림 카키 매트"):
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼 세부모델 1"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_2_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 세부옵션을 선택해주세요!</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0 2WD밴</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("스마트(자동)"):
        #st.session_state.button_state = "세2 스마트(자동)"
        st.session_state.button_state = "main"
    if st.button("스마트 초이스(자동)"):
        #st.session_state.button_state = "세2 스마트 초이스(자동)"
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_3_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 세부옵션을 선택해주세요!</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0터보 액티브 I 2WD</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("스마트(자동)"):
        #st.session_state.button_state = "세3 스마트(자동)"
        st.session_state.button_state = "main"
    if st.button("디 에센셜 라이트(자동)"):
        #st.session_state.button_state = "세3 디 에센셜 라이트(자동)"
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_4_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 세부옵션을 선택해주세요!</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0터보 액티브 II 2WD</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("디 에센셜(자동)"):
        #st.session_state.button_state = "세4 디 에센셜(자동)"
        st.session_state.button_state = "main"
    if st.button("인스퍼레이션(자동)"):
        #st.session_state.button_state = "세4 인스퍼레이션(자동)"
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 캐스퍼_세부모델_5_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 세부옵션을 선택해주세요!</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 국산차 > 현대 > 캐스퍼 > 2023년형 가솔린1.0터보 액티브 I 2WD밴</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("스마트(자동)"):
        #st.session_state.button_state = "세5 스마트(자동)"
        st.session_state.button_state = "main"
    if st.button("스마트 초이스(자동)"):
        #st.session_state.button_state = "세5 스마트 초이스(자동)"
        st.session_state.button_state = "main"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "캐스퍼"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"

def 유럽_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 제조사는 어디인가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 유럽</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("벤츠"):
        st.session_state.button_state = "벤츠"
    if st.button("BMW"):
        st.session_state.button_state = "BMW"
    if st.button("아우디"):
        st.session_state.button_state = "아우디"
    if st.button("폭스바겐"):
        st.session_state.button_state = "폭스바겐"
    if st.button("미니"):
        st.session_state.button_state = "미니"
    if st.button("볼보"):
        st.session_state.button_state = "볼보"
    if st.button("폴스타"):
        st.session_state.button_state = "폴스타"
    if st.button("랜드로버"):
        st.session_state.button_state = "랜드로버"
    if st.button("포르쉐"):
        st.session_state.button_state = "포르쉐"
    if st.button("람보르기니"):
        st.session_state.button_state = "람보르기니"
    if st.button("벤틀리"):
        st.session_state.button_state = "벤틀리"
    if st.button("맥라렌"):
        st.session_state.button_state = "맥라렌"
    if st.button("페라리"):
        st.session_state.button_state = "페라리"
    if st.button("애스턴마틴"):
        st.session_state.button_state = "애스턴마틴"
    if st.button("로터스"):
        st.session_state.button_state = "로터스"
    if st.button("마세라티"):
        st.session_state.button_state = "마세라티"
    if st.button("롤스로이스"):
        st.session_state.button_state = "롤스로이스"
    if st.button("푸조"):
        st.session_state.button_state = "푸조"
    if st.button("이네오스"):
        st.session_state.button_state = "이네오스"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"
        
def 미국_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 제조사는 어디인가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 미국</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("포드"):
        st.session_state.button_state = "포드"
    if st.button("링컨"):
        st.session_state.button_state = "링컨"
    if st.button("지프"):
        st.session_state.button_state = "지프"
    if st.button("GMC"):
        st.session_state.button_state = "GMC"
    if st.button("캐딜락"):
        st.session_state.button_state = "캐딜락"
    if st.button("테슬라"):
        st.session_state.button_state = "테슬라"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"
        
def 일본_buttons():
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>오토커넥트 챗봇 : 원하시는 제조사는 어디인가요?</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: flex-start;'><strong>신차구매 컨설팅 > 수입차 > 일본</strong></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.button("토요타"):
        st.session_state.button_state = "토요타"
    if st.button("렉서스"):
        st.session_state.button_state = "렉서스"
    if st.button("혼다"):
        st.session_state.button_state = "혼다"
    if st.button("이전으로 돌아가기"):
        st.session_state.button_state = "수입차"
    if st.button("처음으로 돌아가기"):
        st.session_state.button_state = "main"
        
# 버튼 상태에 따라 버튼 표시 => 버튼을 누르면 버튼의 상태가 변하고, 버튼의 상태가 변하면 함수가 호출됨
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.session_state.button_state == "main":
    main_buttons()
elif st.session_state.button_state == "신차구매 컨설팅":
    신차구매_컨설팅_buttons()
elif st.session_state.button_state == "중고차구매 컨설팅":
    중고차구매_컨설팅_buttons()
elif st.session_state.button_state == "리스렌트 승계 컨설팅":
    리스렌트_승계_컨설팅_buttons()
elif st.session_state.button_state == "사후관리 컨설팅":
    사후관리_컨설팅_buttons()
elif st.session_state.button_state == "법인 전문 컨설팅 의뢰":
    법인_전문_컨설팅_의뢰_buttons()
elif st.session_state.button_state == "국산차":
    국산차_buttons()
elif st.session_state.button_state == "수입차":
    수입차_buttons()
elif st.session_state.button_state == "최신 인기차량 추천받기":
    최신_인기차량_추천받기_buttons()
elif st.session_state.button_state == "나만의 모빌리티 선택하기":
    나만의_모빌리티_선택하기_buttons()
elif st.session_state.button_state == "현대":
    현대_buttons()
elif st.session_state.button_state == "제네시스":
    제네시스_buttons()
elif st.session_state.button_state == "기아":
    기아_buttons()
elif st.session_state.button_state == "쉐보레":
    쉐보레_buttons()
elif st.session_state.button_state == "KG 모빌리티":
    KG_모빌리티_buttons()
elif st.session_state.button_state == "르노":
    르노_buttons()
elif st.session_state.button_state == "디피코":
    디피코_buttons()
elif st.session_state.button_state == "스마트 EV":
    스마트_EV_buttons()
elif st.session_state.button_state == "마이브":
    마이브_buttons()
elif st.session_state.button_state == "유럽":
    유럽_buttons()
elif st.session_state.button_state == "미국":
    미국_buttons()
elif st.session_state.button_state == "일본":
    일본_buttons()
elif st.session_state.button_state == "벤츠":
    벤츠_buttons()
elif st.session_state.button_state == "BMW":
    BMW_buttons()
elif st.session_state.button_state == "아우디":
    아우디_buttons()
elif st.session_state.button_state == "폭스바겐":
    폭스바겐_buttons()
elif st.session_state.button_state == "미니":
    미니_buttons()
elif st.session_state.button_state == "볼보":
    볼보_buttons()
elif st.session_state.button_state == "폴스타":
    폴스타_buttons()
elif st.session_state.button_state == "랜드로버":
    랜드로버_buttons()
elif st.session_state.button_state == "포르쉐":
    포르쉐_buttons()
elif st.session_state.button_state == "람보르기니":
    람보르기니_buttons()
elif st.session_state.button_state == "벤틀리":
    벤틀리_buttons()
elif st.session_state.button_state == "맥라렌":
    맥라렌_buttons()
elif st.session_state.button_state == "페라리":
    페라리_buttons()
elif st.session_state.button_state == "애스턴마틴":
    애스턴마틴_buttons()
elif st.session_state.button_state == "로터스":
    로터스_buttons()
elif st.session_state.button_state == "마세라티":
    마세라티_buttons()
elif st.session_state.button_state == "롤스로이스":
    롤스로이스_buttons()
elif st.session_state.button_state == "푸조":
    푸조_buttons()
elif st.session_state.button_state == "이네오스":
    이네오스_buttons()
elif st.session_state.button_state == "포드":
    포드_buttons()
elif st.session_state.button_state == "링컨":
    링컨_buttons()
elif st.session_state.button_state == "지프":
    지프_buttons()
elif st.session_state.button_state == "GMC":
    GMC_buttons()
elif st.session_state.button_state == "캐딜락":
    캐딜락_buttons()
elif st.session_state.button_state == "테슬라":
    테슬라_buttons()
elif st.session_state.button_state == "토요타":
    토요타_buttons()
elif st.session_state.button_state == "렉서스":
    렉서스_buttons()
elif st.session_state.button_state == "혼다":
    혼다_buttons()
elif st.session_state.button_state == "캐스퍼":
    캐스퍼_buttons()
elif st.session_state.button_state == "캐스퍼 세부모델 1":
    캐스퍼_세부모델_1_buttons()
elif st.session_state.button_state == "캐스퍼 세부모델 2":
    캐스퍼_세부모델_2_buttons()
elif st.session_state.button_state == "캐스퍼 세부모델 3":
    캐스퍼_세부모델_3_buttons()
elif st.session_state.button_state == "캐스퍼 세부모델 4":
    캐스퍼_세부모델_4_buttons()
elif st.session_state.button_state == "캐스퍼 세부모델 5":
    캐스퍼_세부모델_5_buttons()
elif st.session_state.button_state == "세1 스마트(자동)":
    캐스퍼_세부모델_1_스마트_buttons()
elif st.session_state.button_state == "세1 디 에센셜 라이트(자동)":
    캐스퍼_세부모델_1_디_에센셜_라이트_buttons()
elif st.session_state.button_state == "세1 디 에센셜(자동)":
    캐스퍼_세부모델_1_디_에센셜_buttons()
elif st.session_state.button_state == "세1 인스퍼레이션(자동)":
    캐스퍼_세부모델_1_인스퍼레이션_buttons()
st.markdown('</div>', unsafe_allow_html=True)

# OpenAI API 키 설정
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"  # 적절한 엔진을 선택해주세요.

# 시스템 메시지 설정 (한글)
system_message = '''
당신은 오토커넥트 AI 챗봇입니다. 자신의 정체성이나 역할에 대해 물어보면 '오토커넥트 챗봇'이라고만 소개하세요. 다른 표현을 사용하여 자신을 소개하지 마세요.
만약에 누군가가 당신의 전화번호에 대해서 물어본다면 '010-XXXX-XXXX'라고 친절하게 알려주세요.
누군가 당신에게 '1번' 또는 '1' 또는 '신차구매' 또는 '신차구매 컨설팅'쪽으로 물어본다면 꼭 '신차구매에 관심있으시군요!'라고 말한 뒤에 구매를 희망하는 자동차 종류를 유도하는 질문을 하세요.
'''

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 첫 번째 시스템 메시지를 설정합니다.
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({"role": "system", "content": system_message})

# 버튼을 통해 입력하는 함수
def set_input_text(text):
    st.session_state.input = text
    send_message(text)

# 이전 메시지 표시
for idx, message in enumerate(st.session_state.messages):
    if idx > 0:  # 시스템 메시지를 제외한 메시지만 표시
        role = "사용자" if message["role"] == "user" else "오토커넥트 챗봇"
        st.markdown(f"**{role}:** {message['content']}")

# 콜백 함수 정의
def send_message(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.input = ""  # 입력 필드 초기화

    response = openai.ChatCompletion.create(
        model=st.session_state["openai_model"],
        messages=st.session_state.messages,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    assistant_message = response.choices[0].message["content"].strip()
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    st.experimental_rerun()




# 입력란 생성 및 콜백 연결
st.markdown("<hr>", unsafe_allow_html=True)
st.text_input("무엇을 도와드릴까요? 오토커넥트 챗봇에게 물어보세요!", key="input", on_change=lambda: send_message(st.session_state.input))
