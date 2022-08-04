import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page1():
    st.markdown("# Cover 🌈")
    st.sidebar.markdown("# Cover 🌈")  

def page2():
    st.markdown("# Page 2 🌺")
    st.sidebar.markdown("# Pengertian Cyber Security dan Cyber Crime 🌺")

def page3():
    st.markdown("# Page 3 ❄️")
    st.sidebar.markdown("# Jenis-jenis Cybercrime ❄️")  

def page4():
    st.markdown("# Page 4 🎉")
    st.sidebar.markdown("# Tips & Trick Menghindari cybercrime 🎉")
   

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()