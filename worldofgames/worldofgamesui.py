#worldofgamesui.py

import streamlit as st



pages={
    "Home": [
        st.Page("home.py", title="Homepage")
    ],
    "Games": [
        #st.Page("wordsearch.py", title="Word Search"),
        st.Page("webcamdodger.py", title="Webcam Dodger"),
        st.Page("MemoryGame.py", title="Memory Game"),
        st.Page("GuessGame.py", title="Guessing Game"),
        st.Page("CurrencyGame.py", title="Currency Game")
    ]
}

pg = st.navigation(pages)
pg.run()



