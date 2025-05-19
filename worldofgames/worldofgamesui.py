#worldofgamesui.py

import streamlit as st

st.title("World of Games")


links=[]
links.append(["Snake","/snake"])
links.append(["Tetris","/tetris"])

pages={
    "Home": [
        st.page("worldofgamesui.py", title="Homepage")
        ],
    "Games": [
        st.page("wordsearch.py", title="Word Search"),
        st.page("webcamdodger.py", title="Webcam Dodger (mac)")
    ]
}

pg = st.navigation(pages)
pg.run()

col1, col2 = st.columns(2)
with col1:
    st.write("**Welcome to world of games! A project from my DevOps Course**")
    for link in links:
        #st.page_link(link[1], label=link[0])
        st.page_link("https://google.com", label="page2")

with col2:
    st.write("column1 here")
