import streamlit as st

st.title("Hello World")

with st.echo():
    st.write(st.user)
    st.write(st.user.email)
