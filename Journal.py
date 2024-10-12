import streamlit as st
import os
from cryptography.fernet import Fernet


with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()
    
f = Fernet(key)


folder_path = './entries'
for file_name in os.listdir(folder_path):
    # Check if the file has a .jada extension
    if file_name.endswith('.jada'):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            context = f.decrypt(file.read().encode('utf-8')).decode()

            container = st.container()
            container.columns(3, vertical_alignment="bottom")
            container.caption(context)


st.button("Add Page",icon=":material/add_circle:")
