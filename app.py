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
    "I will analyze your understanding and identify gaps."
)

api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")
user_input = st.text_area("✍️ Explain the concept here", height=160)

def fallback_response(text):
    return f"""
### ✅ What you understood well
- You have a basic idea of the concept.
- Your explanation shows familiarity with key terms.

### ⚠️ Missing or weak areas
- The explanation lacks real-world examples.
- Important sub-concepts are not clearly explained.

### 📘 Correct Explanation
The concept can be better understood by breaking it into smaller parts and explaining how each part works together.

### 🚀 How you can improve
- Add examples
- Explain *why* the concept works, not just *what* it is
- Try teaching it to a beginner in simple words
"""

if st.button("Analyze My Understanding"):
    if not user_input.strip():
        st.warning("Please explain a concept first.")
    else:
        try:
            if api_key:
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=user_input
                )
                st.success("AI Analysis Complete ✅")
                st.markdown(response.text)
            else:
                raise Exception("No API key")

        except Exception:
            st.info("⚠️ AI quota reached. Showing offline analysis mode.")
            st.markdown(fallback_response(user_input))
