import streamlit as st
import re

st.title("TTR 분석기")

text = st.text_area("발화를 입력하세요")

if text:
    tokens = re.findall(r'[가-힣a-zA-Z]+', text.lower())
    num_tokens = len(tokens)
    num_types = len(set(tokens))

    ttr = num_types / num_tokens if num_tokens > 0 else 0

    st.write("총 단어 수:", num_tokens)
    st.write("고유 단어 수:", num_types)
    st.write("TTR:", round(ttr, 4))
