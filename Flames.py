import streamlit as st

def flames_result(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    combined_name = name1 + name2
    flames = "FLAMES"
    
    while len(flames) > 1:
        index = (len(combined_name) % len(flames)) - 1
        flames = flames[:index] + flames[index+1:]

    return flames

# Streamlit UI
st.title("Flames Finder App")

name1 = st.text_input("Enter Name 1:")
name2 = st.text_input("Enter Name 2:")

if st.button("Find Flames"):
    if name1 and name2:
        result = flames_result(name1, name2)
        st.success(f"The Flames result is: {result}")
    else:
        st.warning("Please enter both names before finding Flames.")
