import streamlit as st
from googletrans import Translator, LANGUAGES

translator = Translator()

st.sidebar.title("번.역.기")
st.sidebar.write("Simple web translator using Streamlit&Googletrans")

text= st.text_area("번역할 텍스트를 입력하세요: ")

src_lang=st.selectbox("원본 언어", options=list(LANGUAGES.keys()), format_func=lambda x: LANGUAGES[x])
dest_lang=st.selectbox("번역할 언어", options=list(LANGUAGES.keys()), format_func=lambda x: LANGUAGES[x])

if st.button("번역하기"):
    if text.strip():
        try:
            translated_text=translator.translate(text,src=src_lang,dest=dest_lang).text
            st.success("결과: ")
            st.write(translated_text)
        except Exception as e:
            st.error("번역 중 오류 발생!")
    else:
        st.warning("텍스트를 입력하셔요.")