import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/21.png")

with col2:
    st.title("S.M.Nabil Mushfique")
    content = """
    Hi, I'm Nabil. I'm a student of Department of Software Engineer at Daffodil International University.
    """
    st.info(content)