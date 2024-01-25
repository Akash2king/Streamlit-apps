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
st.session_state["name"] : str =st.text_input('Hello! what is your name')

if st.session_state["name"] :
	st.write('well,I am thinking a number between 1 and 20')

	st.session_state["guess"] :int=st.number_input('take a guess',min_value=0,max_value=20)
	if not "secretnum"  in st.session_state:
		st.session_state["secretnum"] :int = random . randint (1,20)
		st.session_state["guesstaken"] :int =0
	if st.session_state["guesstaken"] >= 6:
			st.markdown(f" # you have'nt found it,  the number is {st.session_state["secretnum"]}refresh to play again ")
			st.cache_data.clear()
			st.stop()
	if st.button("check"):
		st.write(st.session_state)
		if st.session_state["guess"] != st.session_state["secretnum"]:
			st.warning(f"You have remaining {6-st.session_state["guesstaken"]} guesses")
		if st.session_state["guess"] < st.session_state["secretnum"]:
			st.session_state["guesstaken"] +=1
			st.warning("guess is too low")
			
		elif st.session_state["guess"] > st.session_state["secretnum"]:
			st.session_state["guesstaken"] +=1
			st.warning("guess is too high")
		
		elif st.session_state["guess"] == st.session_state["secretnum"]:
			st.success(f''' you won \n
			  you found the number in {st.session_state["guesstaken"]} guesses''')
			
			st.markdown("# refresh to play again..")
