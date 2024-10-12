import streamlit as st
from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# with open('encryption_key.key', 'wb') as key_file:
#     key_file.write(key)
# STORING KEYS(WILL BE CHANGED SYSTEM)

with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()
    
f = Fernet(key)


st.title("How Are You Feeling Today?")
entry = st.text_area("write your feelings", height = 900)

with open("entries/entry.jada", "w") as file:
    file.write(f.encrypt(entry.encode('utf-8')).decode('utf-8'))
    file.write("\n")