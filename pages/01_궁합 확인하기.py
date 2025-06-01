import streamlit as st

# 궁합 정보 사전
mbti_compatibility = {
    ("INFP", "ENFJ"): "감성적인 연결과 이해심이 잘 맞아요. 서로를 깊이 있게 이해할 수 있는 조합입니다.",
    ("INTJ", "ENFP"): "냉철한 전략가와 자유로운 영혼의 환상적인 균형! 서로에게 자극이 되는 궁합이에요.",
    ("ISTJ", "ESFP"): "정반대지만 서로에게 없는 점을 채워줄 수 있어요. 현실과 감성의 만남!",
    ("ISFJ", "ESTP"): "한쪽은 배려심, 다른 한쪽은 추진력! 둘이 만나면 일도 사랑도 척척이에요.",
    ("ENTP", "INFJ"): "아이디어 뱅크와 이상주의자의 대화는 끝이 없어요. 지적이고 감성적인 커넥션!",
    ("ISFP", "ENFJ"): "따뜻한 내향성과 사교적인 외향성의 조화. 서로 잘 챙겨주고 배려해요.",
    # 더 많은 궁합을 원하면 여기에 추가
}

# MBTI 목록
mbti_list = sorted([
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
])

# Streamlit UI
st.title("💑 MBTI 궁합 확인기")

col1, col2 = st.columns(2)
with col1:
    mbti1 = st.selectbox("첫 번째 사람의 MBTI", mbti_list, key="mbti1")
with col2:
    mbti2 = st.selectbox("두 번째 사람의 MBTI", mbti_list, key="mbti2")

if st.button("궁합 확인하기"):
    key = (mbti1, mbti2)
    reverse_key = (mbti2, mbti1)

    if key in mbti_compatibility:
        st.success(f"{mbti1} ❤️ {mbti2} 궁합: {mbti_compatibility[key]}")
    elif reverse_key in mbti_compatibility:
        st.success(f"{mbti1} ❤️ {mbti2} 궁합: {mbti_compatibility[reverse_key]}")
    elif mbti1 == mbti2:
        st.info(f"{mbti1} ❤️ {mbti2}: 같은 성향이라 서로 깊이 이해할 수 있어요.")
    else:
        st.warning("이 조합에 대한 특별한 궁합 정보는 없지만, MBTI는 참고용일 뿐이에요. 마음이 제일 중요하죠!")

