# guess-the-number
import streamlit as st
import random

st.markdown('''
# Guess the Number Game

A simple Python game where the computer selects a random number between 1 and 20, and the player tries to guess it within 6 attempts.

## Gameplay Rules

- The computer randomly selects a secret number between 1 and 20.
- You have a maximum of 6 attempts to guess the correct number.
- After each guess, the program provides feedback on whether your guess is too high or too low.
- If you correctly guess the number within the allowed attempts, you win!
- If you run out of attempts, the program reveals the secret number and you lose.
''')
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.session_state["name"] = st.text_input('Hello! What is your name')

if st.session_state["name"]:
    st.write("Well, I am thinking of a number between 1 and 20")

    st.session_state["guess"] = st.number_input('Take a guess', min_value=0, max_value=20)
    
    if "secretnum" not in st.session_state:
        st.session_state["secretnum"] = random.randint(1, 20)
        st.session_state["guesstaken"] = 0

    if st.session_state["guesstaken"] >= 6:
        sec = st.session_state["secretnum"]
        st.markdown(f"# You haven't found it. The number is {sec}. Refresh to play again.")
        st.cache_data.clear()
        st.stop()

    if st.button("Check"):
        if st.session_state["guess"] != st.session_state["secretnum"]:
            st.warning(f"You have {6 - st.session_state['guesstaken']} guesses remaining.")

        if st.session_state["guess"] < st.session_state["secretnum"]:
            st.session_state["guesstaken"] += 1
            st.warning("Guess is too low")

        elif st.session_state["guess"] > st.session_state["secretnum"]:
            st.session_state["guesstaken"] += 1
            st.warning("Guess is too high")

        elif st.session_state["guess"] == st.session_state["secretnum"]:
            st.success(f'''You won!\nYou found the number in {st.session_state["guesstaken"]} guesses''')

            st.markdown("# Refresh to play again.")
