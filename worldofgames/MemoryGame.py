#MemoryGame

import streamlit as st
import time
import random

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "difficulty" not in st.session_state:
    st.session_state["difficulty"] = 1


st.title(f"Memory Game - Score {st.session_state["score"]}")




def startMemoryGame():
    time.sleep(1.5)
    numberToRemember = random.randint(100000,999999)
    spacingR = random.randint(1,400)
    spacing = "&nbsp;"
    spacing = spacing*spacingR
    placeholder = st.empty()
    placeholder.write(f"# {spacing}**{numberToRemember}**")
    st.session_state["numberToRemember"] = numberToRemember
    roundtime = 1 + (0.1*(5-st.session_state["difficulty"]))
    time.sleep(roundtime)
    placeholder.empty()
    st.chat_input(
        placeholder="What did it say?", 
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
    if guessStr==st.session_state["numberToRemember"]:
        #return 1
        st.success("Yarp!")
        st.session_state["score"] += 100 * st.session_state["difficulty"]
        st.balloons()
    else:
        #return 0
        st.error("Narp!")

    


st.slider(
    label="Difficulty",
    min_value=1,
    max_value=5,
    key="difficulty"
)




startMemoryGame()

