import streamlit as st
from pdfchat import PDFChatbot
import time
import asyncio

def get_chatbot():
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = PDFChatbot()
    return st.session_state.chatbot

async def faq_chatbot():
    if "db" not in st.session_state or not st.session_state.pdf_processed:
        st.warning("Please upload a PDF file first.")
        return

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Ask me anything about the uploaded PDF."}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask your question")
    if prompt:
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):
                chatbot = get_chatbot()
                start = time.time()
                result = chatbot.get_response(prompt)
                end = time.time()
                response_time = round((end - start), 2)
                st.write(result)
                st.markdown(
                    f'<div style="font-size: 0.8em; display: flex; justify-content: flex-end; align-items: center;">'
                    f'<i class="fas fa-clock" style="margin-right: 5px;"></i>'
                    f'Time : {response_time} s'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                st.session_state.messages.append({"role": "assistant", "content": result})

async def main():
    st.set_page_config(page_title="PDF Chatbot")
    st.header("PDF Chatbot")

    if "pdf_processed" not in st.session_state:
        st.session_state.pdf_processed = False

    pdf_file = st.file_uploader("Upload your PDF", type="pdf")

    if pdf_file is not None and not st.session_state.pdf_processed:
        with st.spinner("Processing PDF..."):
            try:
                chatbot = get_chatbot()
                st.session_state.db = chatbot.get_vector_store(pdf_file)
                
                st.session_state.pdf_processed = True
                st.success("PDF processed successfully!")
            except Exception as e:
                st.error(f"Error processing PDF: {str(e)}")
                st.session_state.pdf_processed = False

    if st.session_state.pdf_processed:
        await faq_chatbot()
    else:
        st.info("Please upload a PDF to start chatting.")

if __name__ == "__main__":
    asyncio.run(main())