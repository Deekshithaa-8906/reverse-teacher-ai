import streamlit as st
from google import genai

st.set_page_config(
    page_title="Reverse Teacher AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Reverse Teacher AI")
st.write(
    "Explain a concept in your own words. "
    "I will analyze your understanding and find gaps."
)

api_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password"
)

user_input = st.text_area(
    "✍️ Explain the concept here",
    height=160
)

if st.button("Analyze My Understanding"):
    if not api_key:
        st.warning("Please enter your Gemini API key.")
    elif not user_input.strip():
        st.warning("Please explain a concept first.")
    else:
        try:
            client = genai.Client(api_key=api_key)

            prompt = f"""
You are an expert teacher.

A student explained a concept as follows:
\"\"\"{user_input}\"\"\"

Analyze this and respond with:
1. What the student understands correctly
2. What is missing or incorrect
3. Correct explanation
4. How the student can improve
"""

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            st.success("Analysis Complete ✅")
            st.markdown(response.text)

        except Exception as e:
            st.error("Something went wrong ❌")
            st.code(str(e))
