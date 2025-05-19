#CurrencyGame


import streamlit as st
import time
import random

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "difficulty" not in st.session_state:
    st.session_state["difficulty"] = 1


st.title(f"Currency Game - Score {st.session_state["score"]}")




def startCurrencyGame():
    time.sleep(1.5)
    toGuess = random.randint(1,10*st.session_state["difficulty"])
    st.session_state["toGuess"] = toGuess
    st.write(f"What is ${toGuess} in Shekles")
    st.chat_input(
        placeholder="What did I guess?", 
        key="interface", 
        accept_file=False,max_chars=99, 
        on_submit=guess
        )
    time.sleep(2)
    
    

def guess():
    guessStr = st.session_state["interface"]
    if guessStr==str(st.session_state["toGuess"]*3.4):
        #return 1
        st.success("Yarp!")
        st.session_state["score"] += 100000 * st.session_state["difficulty"]
        st.balloons()

    else:
        #return 0
        st.error(f"Narp! - Sorry bad game - {st.session_state["toGuess"]*3.4}")

    


st.slider(
    label="Difficulty",
    min_value=1,
    max_value=5,
    key="difficulty"
)




startCurrencyGame()

