import streamlit as st
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

# f.encrypt(entry.encode('utf-8')).decode('utf-8')

st.title("How Are You Feeling Today?")
entry = st.text_area("write your feelings", height = 900)

with open("entries/entry.jada", "w") as file:
    file.write(entry + "\n")