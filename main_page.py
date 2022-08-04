# Contents of ~/my_app/main_page.py
import streamlit as st
import time
import requests

from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

with st.spinner('Wait for it...'):
    time.sleep(2)

# st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.title('Menjaga Privasi Online')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

col1, col2 = st.columns(2)

with col1:
    lottie_url = "https://assets9.lottiefiles.com/packages/lf20_llckxtas.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json)

with col2:
    st.header('Kelompok 9')
    st.header('Power Puff Girls 👩‍💻')
    st.subheader('1. Ayu Edwina')
    st.subheader('2. Melisa Aderia')
    st.subheader('3. Ondina Simbolon')






