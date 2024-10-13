import streamlit as st
import pandas as pd
import requests as rs
from cryptography.fernet import Fernet
import csv


st.title('JADA: the App that cares')

database = pd.read_csv('database.csv', header=0)


def get_name():
    return st.session_state.user_state['mail_adress']
def login():
    user_ = database[database['mail_adress'] == mail_adress].copy()
    if len(user_) == 0:
        st.error('User not found')
    else:
        if user_['mail_adress'].values[0] == mail_adress and user_['password'].values[0] == password:
            st.session_state.user_state['mail_adress'] = mail_adress
            st.session_state.user_state['password'] = password
            st.session_state.user_state['logged_in'] = True
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
    st.write('Please login')
    mail_adress = st.text_input('E-Mail')
    password = st.text_input('Password', type='password')
    submit = st.button('Login')

    @st.dialog("Create Login")
    def open_account():
        mail = st.text_input("Email")
        name = st.text_input("Name")
        word = st.text_input("Password", type='password', key='create')

        if st.button("Create"):
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
                    file.write(f"{mail},{name},user,{word},{Fernet.generate_key().decode()},{7770000 + len(lines)}")
                    st.rerun()

    if st.button("Create Login", use_container_width=True):
        open_account()



    # Check if user is logged in
    if submit:
        login()
elif st.session_state.user_state['logged_in']:
    st.write('Welcome to the app')
    st.write('You are logged in as:', get_name())
    st.write('You are a:', st.session_state.user_state['user_type'])
    st.write('Your fixed user message:', st.session_state.user_state['auth_key'])
    if st.session_state.user_state['user_type'] == 'admin':
        st.write('You have admin rights. Here is the database')
        st.table(database)


def get_auth_key():
    return st.session_state.user_state['auth_key']
