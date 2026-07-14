import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
    st.image("images/21.png")

with col2:
    st.title("S.M.Nabil Mushfique")
    content = """
    Hi, I'm Nabil. I'm a student of Department of Software Engineer at Daffodil International University.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])