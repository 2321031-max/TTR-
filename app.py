import streamlit as st
import re
from konlpy.tag import Okt

st.title("TTR 분석기 (기본 / 형태소 분석)")

okt = Okt()

text = st.text_area("발화를 입력하세요")

if text:
    # 기본 TTR
    tokens = re.findall(r'[가-힣a-zA-Z]+', text.lower())
    num_tokens = len(tokens)
    num_types = len(set(tokens))

    ttr_basic = num_types / num_tokens if num_tokens > 0 else 0

    st.subheader("기본 TTR")
    st.write("총 단어 수:", num_tokens)
    st.write("고유 단어 수:", num_types)
    st.write("TTR:", round(ttr_basic, 4))

    # 형태소 분석 TTR
    morphs = okt.morphs(text, stem=True)
    processed = [m for m in morphs if re.match(r'[가-힣a-zA-Z]+', m)]

    num_tokens_stem = len(processed)
    num_types_stem = len(set(processed))

    ttr_stem = num_types_stem / num_tokens_stem if num_tokens_stem > 0 else 0

    st.subheader("형태소 분석 TTR")
    st.write("형태소:", processed)
    st.write("총 단어 수:", num_tokens_stem)
    st.write("고유 단어 수:", num_types_stem)
    st.write("TTR:", round(ttr_stem, 4))
