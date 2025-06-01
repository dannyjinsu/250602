import streamlit as st

def get_mbti_update(mbti):
    updates = {
        "INTJ": "요즘 전략 짜느라 바쁘대. 미래 계획 세우는 중이래.",
        "INTP": "새로운 이론 정리하느라 밤새고 있대. 흥미로운 걸 발견했나 봐!",
        "ENTJ": "프로젝트 리더 맡아서 폭풍처럼 일 처리 중이래.",
        "ENTP": "창업 아이디어 떠올라서 이것저것 실험 중이래.",
        "INFJ": "사람들 도와주느라 요즘 마음이 꽉 찼대.",
        "INFP": "감성 충만하게 글 쓰는 중이래. 영감이 넘친대.",
        "ENFJ": "주변 사람들 잘 챙기고 있대. 요즘 진짜 인기 많대!",
        "ENFP": "새로운 모임에서 친구 잔뜩 사귀는 중이래.",
        "ISTJ": "계획표대로 착실히 살아가는 중이래. 아주 모범생처럼.",
        "ISFJ": "주변 챙기느라 정신 없대. 항상 배려심 넘쳐.",
        "ESTJ": "일 처리하느라 바빠 죽겠대. 효율의 신이래.",
        "ESFJ": "주변 분위기 메이커로 활약 중이래. 다들 그 친구만 찾대.",
        "ISTP": "혼자 뭔가 고치고 만들고 있대. 집중 모드래.",
        "ISFP": "요즘 감성 사진 찍는 데 빠졌대. 자연 속을 떠돌고 있대.",
        "ESTP": "스릴 찾으러 여기저기 다니는 중이래. 액티브하게!",
        "ESFP": "파티와 사람들 속에서 빛나는 중이래. 완전 핫해!"
    }
    return updates.get(mbti, "알 수 없는 MBTI입니다.")

# Streamlit UI
st.title("MBTI 기반 친구 근황 보기")

mbti_list = sorted([
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
])

selected_mbti = st.selectbox("친구의 MBTI를 선택하세요:", mbti_list)

if st.button("근황 보기"):
    result = get_mbti_update(selected_mbti)
    st.success(f"{selected_mbti} 친구 근황: {result}")
