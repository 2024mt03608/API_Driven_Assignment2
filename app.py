

# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8000"

# st.title("🚀 AI Customer Support System")

# # Email Analyzer
# st.header("📧 Email Analyzer")
# email_text = st.text_area("Enter Email")

# if st.button("Analyze"):
#     if email_text:
#         res = requests.post(f"{API_URL}/analyze-email", json={"text": email_text})
#         data = res.json()

#         st.write("### 📌 Category:", data['category'])
#         st.write("### 📊 Confidence:", data['confidence'])
#         st.write("### 😊 Sentiment:", data['sentiment'])
#         st.write("### 🤖 Response:", data['response'])
#     else:
#         st.warning("Please enter email text")

# # Chatbot
# st.header("💬 Support Chatbot")
# query = st.text_input("Ask a question")

# if st.button("Ask"):
#     if query:
#         res = requests.post(f"{API_URL}/chat", json={"text": query})
#         data = res.json()

#         st.write("### 🧠 Answer:", data['answer'])
#     else:
#         st.warning("Please enter a question")



# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8000"

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI Support System", layout="wide")

# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
#     color: white;
# }

# .main-title {
#     font-size: 40px;
#     font-weight: bold;
#     color: #4CAF50;
# }

# .card {
#     padding: 20px;
#     border-radius: 15px;
#     background-color: #1c1f26;
#     box-shadow: 0 4px 10px rgba(0,0,0,0.4);
#     margin-bottom: 20px;
# }

# .metric {
#     font-size: 18px;
#     font-weight: bold;
# }

# .good {color: #4CAF50;}
# .bad {color: #ff4b4b;}
# .neutral {color: #f1c40f;}
# </style>
# """, unsafe_allow_html=True)

# # ---------------- HEADER ----------------
# st.markdown('<p class="main-title">🚀 AI Customer Support System</p>', unsafe_allow_html=True)
# st.markdown("### Intelligent Email Classification + Sentiment + RAG Chatbot")

# # ---------------- LAYOUT ----------------
# col1, col2 = st.columns(2)

# # ---------------- EMAIL ANALYZER ----------------
# with col1:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.subheader("📧 Email Analyzer")

#     email_text = st.text_area("Enter Customer Email", height=150)

#     if st.button("Analyze Email"):
#         if email_text:
#             res = requests.post(f"{API_URL}/analyze-email", json={"text": email_text})
#             data = res.json()

#             # Category
#             st.markdown(f"**📌 Category:** `{data['category']}`")

#             # Confidence color
#             conf = data['confidence']
#             if conf > 0.7:
#                 color = "good"
#             elif conf > 0.4:
#                 color = "neutral"
#             else:
#                 color = "bad"

#             st.markdown(f"**📊 Confidence:** <span class='{color}'>{conf}</span>", unsafe_allow_html=True)

#             # Sentiment
#             sentiment = data['sentiment']
#             sent_color = "good" if sentiment == "POSITIVE" else "bad"

#             st.markdown(f"**😊 Sentiment:** <span class='{sent_color}'>{sentiment}</span>", unsafe_allow_html=True)

#             # Response
#             st.markdown("**🤖 AI Response:**")
#             st.info(data['response'])

#         else:
#             st.warning("Please enter email text")

#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- CHATBOT ----------------
# with col2:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.subheader("💬 Support Chatbot")

#     query = st.text_input("Ask your question")

#     if st.button("Get Answer"):
#         if query:
#             res = requests.post(f"{API_URL}/chat", json={"text": query})
#             data = res.json()

#             st.markdown("**🧠 Answer:**")
#             st.success(data['answer'])
#         else:
#             st.warning("Please enter a question")

#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- FOOTER ----------------
# st.markdown("---")
# st.markdown("Built with ❤️ using NLP + LLM + RAG | Production Ready UI")


# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8000"

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="AI Support System", layout="wide")

# # ---------------- CACHE FUNCTION ----------------
# @st.cache_data
# def call_api(endpoint, payload):
#     res = requests.post(f"{API_URL}/{endpoint}", json=payload)
#     return res.json()

# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
#     color: white;
# }

# .main-title {
#     font-size: 40px;
#     font-weight: bold;
#     color: #4CAF50;
# }

# .card {
#     padding: 20px;
#     border-radius: 15px;
#     background-color: #1c1f26;
#     box-shadow: 0 4px 10px rgba(0,0,0,0.4);
#     margin-bottom: 20px;
# }

# .good {color: #4CAF50;}
# .bad {color: #ff4b4b;}
# .neutral {color: #f1c40f;}
# </style>
# """, unsafe_allow_html=True)

# # ---------------- HEADER ----------------
# st.markdown('<p class="main-title">🚀 AI Customer Support System</p>', unsafe_allow_html=True)
# st.markdown("### Intelligent Email Classification + Sentiment + RAG Chatbot")

# # ---------------- LAYOUT ----------------
# col1, col2 = st.columns(2)

# # ---------------- EMAIL ANALYZER ----------------
# with col1:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.subheader("📧 Email Analyzer")

#     email_text = st.text_area("Enter Customer Email", height=150)

#     if st.button("Analyze Email"):
#         if email_text:
#             with st.spinner("🔍 Analyzing email..."):
#                 data = call_api("analyze-email", {"text": email_text})

#             st.success("Analysis Complete ✅")

#             # Category
#             st.markdown(f"**📌 Category:** `{data['category']}`")

#             # Confidence
#             conf = data['confidence']
#             st.progress(int(conf * 100))

#             if conf > 0.7:
#                 st.success(f"High Confidence ({conf})")
#             elif conf > 0.4:
#                 st.warning(f"Medium Confidence ({conf})")
#             else:
#                 st.error(f"Low Confidence ({conf})")

#             # Sentiment
#             sentiment = data['sentiment']
#             sent_color = "good" if sentiment == "POSITIVE" else "bad"
#             st.markdown(f"**😊 Sentiment:** <span class='{sent_color}'>{sentiment}</span>", unsafe_allow_html=True)

#             # Response
#             st.markdown("**🤖 AI Response:**")
#             st.info(data['response'])

#         else:
#             st.warning("Please enter email text")

#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- CHATBOT ----------------
# with col2:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.subheader("💬 Support Chatbot")

#     query = st.text_input("Ask your question")

#     if st.button("Get Answer"):
#         if query:
#             with st.spinner("💬 Thinking..."):
#                 data = call_api("chat", {"text": query})

#             st.success(data['answer'])
#         else:
#             st.warning("Please enter a question")

#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- FOOTER ----------------
# st.markdown("---")
# st.markdown("Built with ❤️ using NLP + ML + RAG | ⚡ Fast & Production Ready")

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Support", layout="wide")

st.title("🚀 AI Customer Support System")

col1, col2 = st.columns(2)

# ---------------- EMAIL ----------------
with col1:
    st.subheader("📧 Email Analyzer")

    email_text = st.text_area("Enter Email", height=120)

    if st.button("Analyze"):
        if email_text:
            try:
                res = requests.post(f"{API_URL}/analyze-email", json={"text": email_text})
                data = res.json()

                st.write("Category:", data['category'])
                st.write("Confidence:", data['confidence'])
                st.write("Sentiment:", data['sentiment'])
                st.write("Response:", data['response'])

            except:
                st.error("⚠️ API not running. Please start backend.")

        else:
            st.warning("Enter email")


# ---------------- CHAT ----------------
with col2:
    st.subheader("💬 Chatbot")

    query = st.text_input("Ask question")

    if st.button("Ask"):
        if query:
            try:
                res = requests.post(f"{API_URL}/chat", json={"text": query})
                data = res.json()

                st.write("Answer:", data['answer'])

            except:
                st.error("⚠️ API not running.")

        else:
            st.warning("Enter query")