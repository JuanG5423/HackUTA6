import streamlit as st

st.write("Journal Feature")
journal = st.text_area("Write your thoughts here")
if st.button("Save"):
    with open("Pages/JournalDB/journal.txt", "a") as file:
        file.write(journal + "\n")
    st.write("Saved successfully")
    
    st.write("View Journal Entries")
with open("Pages/JournalDB/journal.txt", "r") as file:
    journal_entries = file.readlines()
    for entry in journal_entries:
        st.write(entry)

    