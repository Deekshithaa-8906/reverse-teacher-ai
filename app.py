import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="Reverse Teacher AI", layout="centered")

st.title("🎓 Reverse Teacher AI")
st.write("Explain a concept in your own words. I will analyze your understanding and find gaps.")

# Gemini API key input
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-pro")

    concept = st.text_area("✍️ Explain the concept here:")

    if st.button("Analyze My Understanding"):
        if concept.strip() == "":
            st.warning("Please explain the concept first.")
        else:
            with st.spinner("Analyzing your explanation..."):
                prompt = f"""
                A student explained a concept as follows:

                "{concept}"

                Analyze this explanation.
                1. Identify missing concepts or gaps.
                2. Point out misconceptions if any.
                3. Suggest how the student can improve their understanding.
                Keep the tone friendly and encouraging.
                """

                response = model.generate_content(prompt)
                st.success("Analysis Complete ✅")
                st.write(response.text)
else:
    st.info("Please enter your Gemini API key to continue.")
