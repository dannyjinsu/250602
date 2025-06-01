import streamlit as st
import datetime
from PIL import Image

# 예시용 BMTI 유형
bmti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# Streamlit 앱 기본 설정
st.set_page_config(page_title="오늘의 BMTI 밈", page_icon="😆", layout="centered")
st.title("🎭 오늘의 BMTI 밈")

# 사용자 입력
selected_type = st.selectbox("당신의 BMTI 유형을 선택하세요", bmti_types)

# 이미지 로딩 및 표시
if selected_type:
    st.subheader(f"오늘의 {selected_type} 밈")
    # 업로드한 이미지 불러오기
    image = Image.open("/mnt/data/944cfbcd-4a7c-448b-aae8-eb6159d90e29.png")
    st.image(image, caption=f"{selected_type}를 위한 밈", use_column_width=True)
