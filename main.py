import streamlit as st
import datetime
import pandas as pd
import numpy as np

from api import *
from app.app import *


html_1 = "<p style ='text-align: left'><img src='data:image/png;base64,{}' class='img-fluid' width =100%></p>".format(
    img_to_bytes("static/001.png")
)
st.markdown(
    html_1, unsafe_allow_html=True,
)

html_2 = "<p style ='text-align: left'><img src='data:image/png;base64,{}' class='img-fluid' width =100%></p>".format(
    img_to_bytes("static/002.png")
)
st.markdown(
    html_2, unsafe_allow_html=True,
)


with st.expander("it") :    
    html_3 = "<p style ='text-align: left'><img src='data:image/png;base64,{}' class='img-fluid' width =100%></p>".format(
    img_to_bytes("static/003.png")
    )
    st.markdown(html_3, unsafe_allow_html=True)

with st.expander("idc") :
    html_4 = "<p style ='text-align: left'><img src='data:image/png;base64,{}' class='img-fluid' width =100%></p>".format(
    img_to_bytes("static/004.png")
    )
    st.markdown(html_4, unsafe_allow_html=True)

with st.expander("Biz") :
    html_5 = "<p style ='text-align: left'><img src='data:image/png;base64,{}' class='img-fluid' width =100%></p>".format(
    img_to_bytes("static/005.png")
    )
    st.markdown(html_5, unsafe_allow_html=True)

with st.expander('경영기획') :
    html_6 = "<p style ='text-align: left'><img src='data:image/png;base64,{}' class='img-fluid' width =100%></p>".format(
    img_to_bytes("static/006.png")
    )
    st.markdown(html_6, unsafe_allow_html=True)

with st.expander('우리의 복지가 궁금해?') :
    html_7 = "<p style ='text-align: left'><img src='data:image/png;base64,{}' class='img-fluid' width =100%></p>".format(
    img_to_bytes("static/007.png")
    )
    st.markdown(html_7, unsafe_allow_html=True)
    st.write("--------------------")
    html_8 = "<p style ='text-align: left'><img src='data:image/png;base64,{}' class='img-fluid' width =100%></p>".format(
    img_to_bytes("static/008.png")
    )
    st.markdown(html_8, unsafe_allow_html=True)


col_1, col_2, col_3, col_4, col_5 = st.columns(5) 
if col_3.button('지원하러 가기') :
    st.markdown("<h1 style='text-align: center; color: black;'>32' 상반기 kt cloud 신입/경력 채용</h1>", unsafe_allow_html=True)
    option = st.selectbox("직무 선택" , ('IT',"IDC", "경영기획" ,"Biz"))
    input_user_name = st.text_input(label="이름", placeholder="이름 기입")
    radio_gender = st.radio(label="성별", options=["남성", "여성"])
    d = st.date_input(
        "입사 가능일",
        datetime.date(2022, 6, 27))

    agree = st.checkbox('제 3자 정보제공에 동의합니다. (필수)')

    if agree:
        st.error('정보 제공에 동의했습니다.')

    uploaded_files = st.file_uploader("자기소개서/포트폴리오", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

    col1, col2, col3,col4,col5 = st.columns(5) 

    if col3.button("지원 완료") :
        st.balloons()
        st.markdown("<h3 style='text-align: center; color: black;'>지원해주셔서 감사합니다.</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: black;'>지원자의 모든 발걸음을 응원합니다!</h3>", unsafe_allow_html=True)


