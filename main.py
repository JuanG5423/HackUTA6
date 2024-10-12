import streamlit as st

st.title("Your App Title")
st.write("Description or main content here")

#Make journal feature where you can write your thoughts and save them
st.write("Journal Feature")
journal = st.text_area("Write your thoughts here")
if st.button("Save"):
    with open("journal.txt", "a") as file:
        file.write(journal + "\n")
    st.write("Saved successfully")

#Make a feature to view your saved journal entries
st.write("View Journal Entries")
with open("journal.txt", "r") as file:
    journal_entries = file.readlines()
    for entry in journal_entries:
        st.write(entry)

#Make an account feature where you can sign up and log in
st.write("Account Feature")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Sign Up"):
    with open("accounts.txt", "a") as file:
        file.write(f"{username},{password}\n")
    st.write("Account created successfully")
if st.button("Log In"):
    with open("accounts.txt", "r") as file:
        accounts = file.readlines()
        for account in accounts:
            if account.startswith(f"{username},{password}"):
                st.write("Logged in successfully")
                break
        else:
            st.write("Invalid credentials")
