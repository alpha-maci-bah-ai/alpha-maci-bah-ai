import streamlit as st

st.set_page_config(page_title="ALPHA MACI BAH AL - AI", page_icon="🇬🇳")

st.markdown("""
<h1 style='text-align:center;'>🇬🇳 ALPHA MACI BAH AL 🇬🇳</h1>
<h3 style='text-align:center;'>Je suis Peulh, berger de Guinée<br>Fils du Fouta, enfants des montagnes et des plaines.</h3>
""", unsafe_allow_html=True)

st.image("https://i.imgur.com/8Km9tLL.png", use_container_width=True)

st.success("Bienvenue sur l'IA officielle de ALPHA MACI BAH AL - Fierté Peulh du Fouta Djallon !")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Écris ton message à Alpha..."):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    reponse = f"Waaw Alpha ! Tu as dit : '{prompt}'. Je suis ton IA ALPHA MACI BAH AL, berger Peulh, fils du Fouta. Je suis là pour toi ! 🇬🇳🔥"
    st.session_state.messages.append({"role":"assistant","content":reponse})
    st.chat_message("assistant").write(reponse)
