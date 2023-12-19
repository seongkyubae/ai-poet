from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI
chat_model=ChatOpenAI()


st.title('인공지능 연예인 알려줌')
content = st.text_input('연예인의 이름을 제시해주세요')


if st.button('연예인의 정보 요청하기'):
    result =chat_model.predict("연예인" + content + "에 대해 알려줘")
    print(result)
    st.write(result)
