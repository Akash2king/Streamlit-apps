import requests
import streamlit as st
from urllib.request import urlopen
from bs4 import BeautifulSoup

API_URL = "https://api-inference.huggingface.co/models/pszemraj/led-large-book-summary"
key=st.secrets["auth_key"]
headers = {"Authorization": f"Bearer {key}"}

st.title("Doc Summarizer 🔗")

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def get_txt_from_url(urlinput):
    url = urlinput
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

input_option = st.selectbox("Select input option", ["Text Area", "URL", "Upload Text File"])

if input_option == "Text Area":
    input_text = st.text_area("Enter text to summarize")
    if st.button("Summarize"):
        output = query({"inputs": input_text})
        code=output[0]["summary_text"]
        st.write(output[0]["summary_text"])

elif input_option == "URL":
    input_url = st.text_input("Enter URL")
    if st.button("Summarize"):
       
        content=get_txt_from_url(input_url)
        output = query({"inputs": content})
        st.write(output[0]["summary_text"])
        

elif input_option == "Upload Text File":
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    if uploaded_file is not None:
        file_contents = uploaded_file.read().decode("utf-8")
        if st.button("Summarize"):
            output = query({"inputs": file_contents})
            st.write(output[0]["summary_text"])