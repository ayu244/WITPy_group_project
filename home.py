import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page3():
    st.markdown("# Page 3 ❄️")
    st.sidebar.markdown("# Page 3 ❄️")  

def page4():
    st.markdown("# Page 4 🎉")
    st.sidebar.markdown("# Page 4 🎉")
   

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 3": page3,
    "Page 4": page4,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()