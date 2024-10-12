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

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")
    tile.write("journal stuff")

