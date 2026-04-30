import streamlit as st
from konlpy.tag import Okt

# 페이지 제목
st.title("한국어 TTR(Type-Token Ratio) 계산기")

# KoNLPy 객체 생성 (캐싱하여 성능 최적화)
@st.cache_resource
def get_okt():
    return Okt()

def calculate_ttr(text):
    okt = get_okt()
    # 형태소 분석 및 품사 태깅
    morphemes = okt.pos(text, norm=True, stem=True)
    
    # 내용어(명사, 동사, 형용사)만 추출
    content_morphemes = [word for word, pos in morphemes if pos in ['Noun', 'Verb', 'Adjective']]
    
    if not content_morphemes:
        return 0.0, [], []

    total_tokens = len(content_morphemes)
    unique_types = set(content_morphemes)
    num_unique_types = len(unique_types)
    
    ttr = num_unique_types / total_tokens
    
    return ttr, list(unique_types), content_morphemes

# 사용자 입력 UI
user_utterance = st.text_input("분석할 한국어 발화를 입력하세요:", placeholder="예: 어제 먹은 사과는 정말 맛있는 사과였다.")

if user_utterance:
    ttr_value, types, tokens = calculate_ttr(user_utterance)

    # 결과 출력 섹션
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("TTR (Type-Token Ratio)", f"{ttr_value:.4f}")
    with col2:
        st.metric("총 토큰 / 고유 타입", f"{len(tokens)} / {len(types)}")

    st.subheader("상세 분석 결과")
    st.write("**추출된 내용 형태소 (Tokens):**")
    st.info(", ".join(tokens))
    
    st.write("**고유한 형태소 (Types):**")
    st.success(", ".join(types))
