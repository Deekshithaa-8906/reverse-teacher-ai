import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(
    page_title="Reverse Teacher AI",
    layout="centered"
)

st.title("🎓 Reverse Teacher AI")
st.write(
    "Explain a concept in your own words. "
    "I will analyze your understanding and identify gaps."
)

# Gemini API key input
api_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password"
)

# User explanation input
user_input = st.text_area(
    "✍️ Explain the concept here",
    height=200
)

if st.button("Analyze My Understanding"):
    if not api_key:
        st.warning("Please enter your Gemini API key.")
    elif not user_input.strip():
        st.warning("Please explain the concept first.")
    else:
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)

            # ✅ CORRECT MODEL (WORKING)
            model = genai.GenerativeModel("models/gemini-1.5-flash")

            prompt = f"""
You are an expert teacher.

A student explained a concept as follows:
\"\"\"{user_input}\"\"\"

Tasks:
1. Identify what the student understands correctly
2. Identify missing or weak concepts
3. Give constructive feedback
4. Suggest how the student can improve

Be clear, supportive, and educational.
"""

            response = model.generate_content(prompt)

            st.subheader("🧠 Analysis Result")
            st.write(response.text)

        except Exception as e:
            st.error("Something went wrong while calling Gemini API.")
            st.exception(e)

