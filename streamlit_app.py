import streamlit as st

# 1. 페이지 설정 (웹 브라우저 탭에 표시될 내용)
st.set_page_config(
    page_title="홍길동의 자기소개",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 (프로필 사진 및 연락처)
with st.sidebar:
    st.header("Contact Me")
    # 본인의 사진 URL이 있다면 넣어주세요 (없으면 placeholder 유지)
    st.image("https://via.placeholder.com/150", caption="홍길동 (Gildong Hong)")
    st.write("📧 이메일: hong@example.com")
    st.write("🔗 [GitHub](https://github.com)")
    st.write("💼 [LinkedIn](https://linkedin.com)")

# 3. 메인 화면 - 타이틀 및 소개
st.title("👋 안녕하세요, 홍길동입니다!")
st.subheader("💡 문제를 해결하는 개발자가 되기 위해 노력하고 있습니다.")

st.markdown("---")

# 4. 내 소개 (About Me)
st.header("📋 About Me")
st.write(
    """
    안녕하세요! 저는 파이썬과 데이터 분석, 그리고 웹 개발에 관심이 많은 홍길동입니다. 
    새로운 기술을 배우고 그것을 활용해 실생활의 불편함을 해결하는 것을 좋아합니다.
    """
)

# 5. 기술 스택 (Skills) - 컬럼으로 나누어 배치
st.header("🛠️ Skills")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Languages & Frameworks")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- HTML / CSS")

with col2:
    st.subheader("Tools & Database")
    st.write("- Git / GitHub")
    st.write("- MySQL")
    st.write("- VS Code")

st.markdown("---")

# 6. 방명록 기능 (인터랙티브 요소)
st.header("💬 방명록")
st.write("방문해주셔서 감사합니다! 한 줄 인사를 남겨주세요.")

# 사용자 입력 받기
visitor_name = st.text_input("이름", placeholder="홍길순")
visitor_message = st.text_area("메시지", placeholder="반갑습니다! 응원합니다.")

if st.button("남기기"):
    if visitor_name and visitor_message:
        st.success(f"🎉 {visitor_name}님의 메시지가 등록되었습니다! (실제 저장은 데이터베이스 연결이 필요합니다)")
        st.info(f"**[{visitor_name}]**: {visitor_message}")
    else:
        st.warning("이름과 메시지를 모두 입력해주세요!")