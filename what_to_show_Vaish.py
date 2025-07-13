import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Dear Vaishnavi❤️", layout="centered")

# Use session state to simulate "windows"
if "page" not in st.session_state:
    st.session_state.page = "home"

# Go back to home
if st.button("⬅ Back", key="back", help="Go back") and st.session_state.page != "home":
    st.session_state.page = "home"

# --- PAGE: Funny Window ---
if st.session_state.page == "funny":
    st.markdown("### I miss you :(")
    st.image(Image.open("Funny_Sad_Cat.png"), width=250)

# --- PAGE: Image Grid ---
elif st.session_state.page == "grid":

    col1, col2 = st.columns(2)
    with col1:
        st.image(Image.open("Image1.png").resize((400,400)))
    with col2:
        st.image(Image.open("Image2.png").resize((400,400)))

    col3, col4 = st.columns(2)
    with col3:
        st.image(Image.open("Image3.png").resize((400,400)))
    with col4:
        st.image(Image.open("Image4.png").resize((400,400)))

    if st.button("Remember us?", key="funny_btn"):
        st.session_state.page = "funny"
        st.rerun()

# --- PAGE: Home ---
else:
    st.title("❤️  Dear Vaishnavi ❤️")
    if st.button("Click me"):
        st.session_state.page = "grid"
        st.rerun()

