import streamlit as st
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Reverse Teacher AI",
    page_icon="🎓",
    layout="centered"
)

# ---------------- UI ----------------
st.title("🎓 Reverse Teacher AI")
st.write(
    "Explain a concept in your own words. "
    "I will analyze your understanding and identify gaps."
)

# ---------------- INPUTS ----------------
api_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password"
)

user_input = st.text_area(
    "✍️ Explain the concept here",
    height=150,
    placeholder="Example: Python is an object oriented programming language..."
)

analyze_btn = st.button("Analyze My Understanding")

# ---------------- LOGIC ----------------
if analyze_btn:
    if not api_key:
        st.warning("⚠️ Please enter your Gemini API key.")
    elif not user_input.strip():
        st.warning("⚠️ Please explain a concept before clicking analyze.")
    else:
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)

            # ✅ CORRECT MODEL (IMPORTANT)
            model = genai.GenerativeModel("gemini-1.5-flash")


            prompt = f"""
You are an expert teacher.

A student explained a concept as follows:
\"\"\"{user_input}\"\"\"

Your tasks:
1. Identify what the student understands correctly
2. Identify missing or weak concepts
3. Give constructive feedback
4. Suggest how the student can improve

Be clear, supportive, and educational.
"""

            response = model.generate_content(prompt)

            st.success("✅ Analysis Complete")
            st.markdown(response.text)

        except Exception as e:
            st.error("❌ Something went wrong while calling Gemini API.")
            st.code(str(e))

