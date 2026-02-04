import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Reverse Teacher AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Reverse Teacher AI")
st.write(
    "Explain a concept in your own words. "
    "I will analyze your understanding and identify gaps."
)

api_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password"
)

user_input = st.text_area(
    "✍️ Explain the concept here",
    height=150
)

if st.button("Analyze My Understanding"):
    if not api_key:
        st.warning("Please enter your Gemini API key.")
    elif not user_input.strip():
        st.warning("Please explain a concept first.")
    else:
        try:
            genai.configure(api_key=api_key)

            # ✅ STREAMLIT-COMPATIBLE MODEL
            model = genai.GenerativeModel("gemini-1.0-pro")

            prompt = f"""
You are an expert teacher.

A student explained a concept as follows:
\"\"\"{user_input}\"\"\"

1. What the student understands correctly
2. What is missing or incorrect
3. Correct explanation
4. How the student can improve
"""

            response = model.generate_content(prompt)

            st.success("Analysis Complete ✅")
            st.markdown(response.text)

        except Exception as e:
            st.error("Gemini API error ❌")
            st.code(str(e))
