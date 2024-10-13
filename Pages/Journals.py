import streamlit as st  
import os
from cryptography.fernet import Fernet

st.title("Write Your Mind")

# key = Fernet.generate_key()
# with open('encryption_key.key', 'wb') as key_file:
#     key_file.write(key)
# STORING KEYS(WILL BE CHANGED SYSTEM)

with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()
    
f = Fernet(key)


st.title("Journay Entry 1:")
entry = st.text_area("write your feelings", height = 900)

with open("entries/entry.jada", "w") as file:
    file.write(f.encrypt(entry.encode('utf-8')).decode('utf-8'))
    file.write("\n")
    


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