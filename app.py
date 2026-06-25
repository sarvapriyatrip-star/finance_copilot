import streamlit as st
from finance_copilot import get_response

st.set_page_config(
    page_title="Finance Copilot",
    page_icon="💼"
)

st.title("💼 Finance Copilot")
st.subheader("📊 AI Assistant for Finance Professionals")
st.caption("Created by Sarvapriya Tripathi | Built by Python • LangChain • Gemini • Streamlit")

question = st.text_input("Ask a finance question")

if st.button("🚀 Generate"):

    if question:

        st.chat_message("user").write(question)

        with st.spinner("Analyzing your question..."):

            answer = get_response(question)

        st.chat_message("assistant").write(answer)