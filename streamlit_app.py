import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🎬 Disney & Pixar AI Quiz")

# Difficulty selection
difficulty = st.selectbox("Choose your difficulty:", ["Easy", "Medium", "Hard"])

if st.button("Generate Quiz"):
    with st.spinner("Creating your quiz..."):
        prompt = f"""
        Create a 20-question Disney and Pixar quiz.
        Difficulty: {difficulty}

        Format:
        Question:
        A.
        B.
        C.
        D.
        Answer:
        Explanation:
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        st.session_state.quiz = response.choices[0].message.content
        st.session_state.score = 0
        st.session_state.current_q = 0

# Display quiz
if "quiz" in st.session_state:
    st.write(st.session_state.quiz)

    user_score = st.number_input("Enter your score after completing:", min_value=0, max_value=20)

    if st.button("Get Results"):
        if user_score <= 7:
            result = "🎈 Casual Fan"
        elif user_score <= 14:
            result = "🎥 Pixar Pro"
        else:
            result = "🏆 Ultimate Disney Scholar"

        st.subheader("Your Result:")
        st.write(result)