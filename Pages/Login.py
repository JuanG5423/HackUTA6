import streamlit as st
import pandas as pd
import requests as rs
import pathlib
from cryptography.fernet import Fernet
import csv

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
        
css_path = pathlib.Path("Pages/style.css")
load_css(css_path)

col1, col2, col3 = st.columns([2,4,2])
top = st.container()
middle = st.container()
bottom = st.container()

with col2:
    st.image("Assets/JADALOGO.png", use_column_width=True)

# with col3:
#     st.image("Assets/JADAAI.png", width=150)
    
database = pd.read_csv('database.csv', header=0)

pass_key = b'-fguMgQqf6smHyZyo-Boqpm99UGfOhL94dfLOk4Vu9M='
cypher = Fernet(pass_key)

def get_name():
    return st.session_state.user_state['name_surname']
def login():
    user_ = database[database['mail_adress'] == mail_adress].copy()
    if len(user_) == 0:
        st.error('User not found')
    else:
        if user_['mail_adress'].values[0] == mail_adress and (cypher.decrypt(user_['password'].values[0].encode())).decode() == password:
            st.session_state.user_state['mail_adress'] = mail_adress
            st.session_state.user_state['password'] = password
            st.session_state.user_state['logged_in'] = True
            st.session_state.user_state['name_surname'] = user_['name_surname'].values[0]
            st.session_state.user_state['user_type'] = user_['user_type'].values[0]
            st.session_state.user_state['mail_adress'] = user_['mail_adress'].values[0]
            st.session_state.user_state['auth_key'] = user_['auth_key'].values[0]
            st.session_state.user_state['user_ID'] = user_['user_ID'].values[0]

            st.write('You are logged in')
            st.rerun()
        else:
            st.write('Invalid username or password')
if not st.session_state.user_state['logged_in']:
    # Create login form
    mail_adress = st.text_input('E-Mail')
    password = st.text_input('Password', type='password')
    submit = st.button('Login', key="login")

    @st.dialog("Create Login")
    def open_account():
        mail = st.text_input("Email")
        name = st.text_input("Name")
        word = st.text_input("Password", type='password', key='create')

        if st.button("Create",key="c"):
            with open("database.csv", 'a+', newline='') as file:
                file.seek(0)  # Move the cursor to the start of the file
                reader = csv.reader(file)
                lines = list(reader)  # Read all existing lines

                # Check for duplicate email
                existing_emails = [line[0] for line in lines if line]  # Get all existing emails from the first column
                if mail in existing_emails:
                    st.error("Email already exists. Please use a different email.")
                else:
                    # Write the new entry
                    file.write("\n")
                    file.write(f"{mail},{name},user,{cypher.encrypt(word.encode()).decode()},{Fernet.generate_key().decode()},{7770000 + len(lines)}")
                    st.rerun()

    if st.button("Create Login", use_container_width=True, key="Create"):
        open_account()



    # Check if user is logged in
    if submit:
        login()
        
elif st.session_state.user_state['logged_in']:
    st.write('Hi, welcome, ', get_name())
    with st.expander("Menu"):
        st.text("Access Your Journal")
        st.page_link("Pages/Journal.py", label= "Journal", icon=":material/book:")
        st.markdown("-------")
            
        st.text("Know The Team")
        st.page_link("Pages/Aboutus.py", label= "The Team", icon=":material/groups:")
        
        st.text("Home")
        st.page_link("Pages/Home.py", label="Home", icon=":material/nest_eco_leaf:")
        
        if st.button("Logout", use_container_width=True):
            st.session_state.user_state = {
            'name_surname': '',
            'password': '',
            'logged_in': False,
            'user_type': '',
            'mail_adress': '',
            'auth_key': '',
            'user_ID': ''
            }
            st.rerun()
        if st.session_state.user_state['user_type'] == 'admin':
            st.write('You have admin rights. Here is the database')
            st.table(database)


def get_auth_key():
    return st.session_state.user_state['auth_key']

def decrypt_journal(message : str):
    key = get_auth_key()
    f = Fernet(key)
    return f.decrypt(message.encode('utf-8')).decode()