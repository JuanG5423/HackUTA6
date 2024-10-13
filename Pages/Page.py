import streamlit as st
from cryptography.fernet import Fernet
from Pages.Login import get_auth_key
import datetime
# key = Fernet.generate_key()
# with open('encryption_key.key', 'wb') as key_file:
#     key_file.write(key)
# STORING KEYS(WILL BE CHANGED SYSTEM)

key = get_auth_key()
    
f = Fernet(key)
time_stamp = datetime.datetime.now()

st.write(st.session_state)
st.title("How Are You Feeling Today?")
entry = st.text_area("write your feelings", height = 900)

with open("entries/"+ str(st.session_state.user_state['user_ID']) +"entry" + time_stamp.strftime("%d%m%Y") + ".jada", "w") as file:
    file.write(f.encrypt(entry.encode('utf-8')).decode('utf-8'))
    file.write("\n")