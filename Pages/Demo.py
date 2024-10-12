import streamlit as st

st.write("Journal Feature")
journal = st.text_area("Write your thoughts here")
if st.button("Save"):
    with open("/home/unknown/HackUTA6/Pages/JournalDB/journal.txt", "a") as file:
        file.write(journal + "\n")
    st.write("Saved successfully")
    
    st.write("View Journal Entries")
with open("/home/unknown/HackUTA6/Pages/JournalDB/journal.txt", "r") as file:
    journal_entries = file.readlines()
    for entry in journal_entries:
        st.write(entry)

    