#home.py

import streamlit as st
st.title("World of Games")

col1, col2 = st.columns(2)
with col1:
    st.write("**Welcome to world of games! A project from my DevOps Course**")
    st.write("Please help yourself to a game from the menu to the right")

with col2:
    st.write(" ")
