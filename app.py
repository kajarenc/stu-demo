import streamlit as st

st.title("Hello World")

with st.echo():
    st.write(st.user)
    st.write(st.user.email)


if st.user.email:
    st.write(
        "You are not logged in :( Please log in with SSO to see your email address.")
else:
    st.write(f"You are logged in as {st.user.email}!")

if st.user.email == "ben@streamlit.io":
    st.write("You are logged in as Ben!")
    st.balloons()
