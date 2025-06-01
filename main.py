import streamlit as st
import datetime

# 예시용 BMTI 유형
bmti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# BMTI 유형별 이미지 URL 매핑 (Unsplash 또는 picsum.photos 링크 사용)
bmti_memes = {
    "INTJ": "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    "ENTP": "https://picsum.photos/id/1025/600/400",
    "INFP": "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d",
    "ISFP": "https://picsum.photos/id/237/600/400",
    # 나머지 유형은 기본 이미지로 대체됨
}

# 기본 이미지 (유형이 등록되지 않은 경우)
default_meme = "https://picsum.photos/seed/default/600/400"

# Streamlit 앱
st.set_page_config(page_title="오늘의 BMTI 밈", page_icon="😆", layout="centered")
st.title("🎭 오늘의 BMTI 밈")

selected_type = st.selectbox("당신의 BMTI 유형을 선택하세요", bmti_types)

if selected_type:
    meme_url = bmti_memes.get(selected_type, default_meme)
    st.subheader(f"오늘의 {selected_type} 밈")
    st.image(meme_url, caption=f"{selected_type}를 위한 밈", use_column_width=True)
