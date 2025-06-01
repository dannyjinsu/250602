import streamlit as st
import datetime

# 예시용 BMTI 유형
bmti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# BMTI 유형별 밈 이미지 URL 매핑 (예시 URL 사용)
bmti_memes = {
    "INTJ": "https://i.imgur.com/8Km9tLL.jpg",
    "ENTP": "https://i.imgur.com/N9bGv6M.jpg",
    "INFP": "https://i.imgur.com/WxNkK38.jpg",
    "ISFP": "https://i.imgur.com/AF1xUoY.jpg",
    # 나머지도 동일하게 추가 가능
}

def get_today_meme(bmti_type):
    # 날짜 기반 랜덤 시드처럼 하루에 하나만 고정되게
    today = datetime.date.today()
    key = f"{bmti_type}-{today}"
    # 단순히 하루에 하나의 밈을 보여주는 고정 방식 (여기선 그냥 URL 하나 반환)
    return bmti_memes.get(bmti_type, "https://i.imgur.com/YOJ4wmF.png")  # default meme

# Streamlit 앱
st.set_page_config(page_title="오늘의 BMTI 밈", page_icon="😆", layout="centered")

st.title("🎭 오늘의 BMTI 밈")

selected_type = st.selectbox("당신의 BMTI 유형을 선택하세요", bmti_types)

if selected_type:
    meme_url = get_today_meme(selected_type)
    st.subheader(f"오늘의 {selected_type} 밈")
    st.image(meme_url, caption=f"{selected_type}를 위한 밈", use_column_width=True)
