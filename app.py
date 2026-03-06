import streamlit as st
import time
from chatbot_engine import get_answer

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.markdown("""
<style>

/* Soft background */
.stApp {
    background: linear-gradient(135deg, #f5f7fa, #eef2f7);
}

/* Center chat content */
.block-container {
    max-width: 800px;
    padding-top: 2rem;
    margin: auto;
}

/* Chat bubbles styling */
[data-testid="stChatMessage"] {
    border-radius: 12px;
    padding: 10px;
}

/* User message color */
[data-testid="stChatMessage"][data-testid*="user"] {
    background-color: #e3f2fd;
}

/* Bot message color */
[data-testid="stChatMessage"][data-testid*="assistant"] {
    background-color: #f1f8e9;
}

/* Input box styling */
textarea {
    border-radius: 10px !important;
}

/* Title style */
h1 {
    text-align: center;
}

/* Caption alignment */
.stCaption {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖 Appliance FAQ Chatbot")
st.caption("Ask appliance related questions")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:

    avatar = "👤" if msg["role"] == "user" else "🤖"

    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

        if msg.get("confidence"):
            st.caption(f"Confidence: {msg['confidence']:.2%}")
# User input
user_input = st.chat_input("Ask your question...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar="👤"):
      st.write(user_input)

    with st.chat_message("assistant", avatar="🤖"):

        placeholder = st.empty()

        for i in range(3):
            placeholder.write("Thinking" + "." * (i+1))
            time.sleep(0.4)

        answer, confidence = get_answer(user_input)

        placeholder.write(answer)

        st.caption(f"Confidence: {confidence:.2%}")

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "confidence": confidence
    })