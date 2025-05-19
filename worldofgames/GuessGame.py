#GuessGame


import streamlit as st
import time
import random

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "difficulty" not in st.session_state:
    st.session_state["difficulty"] = 1


st.title(f"Guess Game - Score {st.session_state["score"]}")




def startGuessGame():
    time.sleep(1.5)
    guessed = random.randint(1,1+st.session_state["difficulty"])
    st.session_state["guess"] = guessed
    st.chat_input(
        placeholder="What did I guess?", 
        key="interface", 
        accept_file=False,max_chars=99, 
        on_submit=guess
        )
    time.sleep(2)
    
    

def guess():
    guessStr = st.session_state["interface"]
    try:
        guessStr=int(guessStr)
    except:
        guessStr=9
    if guessStr==st.session_state["guess"]:
        #return 1
        st.success("Yarp!")
        st.session_state["score"] += 100000 * st.session_state["difficulty"]
        st.balloons()
        st.balloons()
        st.balloons()
        st.balloons()
    else:
        #return 0
        st.error("Narp! - Sorry bad game")

    


st.slider(
    label="Difficulty",
    min_value=1,
    max_value=5,
    key="difficulty"
)




startGuessGame()

