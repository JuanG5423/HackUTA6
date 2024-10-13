import streamlit as st
top = st.container()
middle = st.container()
bottom = st.container()

def click(button_active):
    if button_active == True:
        st.text(
            "JADA is a Journaling AI Detection App.\nAnger, joy, sadness, write your mind down\nand see what JADA thinks"
        )

with top:
    with st.expander("What is JADA?"):
        if 'button_active' not in st.session_state:
            st.session_state['button_active'] = False

# Create a button
        if st.button("Jada?", icon=":material/sentiment_satisfied:", key='Jada'):
    # Toggle the button's state each time it's clicked
            st.session_state['button_active'] = not st.session_state['button_active']
        click(st.session_state['button_active'])
        
        
        
# st.markdown("----------------")
# st.write("Journal Feature")
# journal = st.text_area("Write your thoughts here")
# if st.button("Save"):
#     with open("/home/unknown/HackUTA6/Pages/JournalDB/journal.txt", "a") as file:
#         file.write(journal + "\n")
#     st.write("Saved successfully")
    
    st.write("View Journal Entries")
with open("/home/unknown/HackUTA6/Pages/JournalDB/journal.txt", "r") as file:
    journal_entries = file.readlines()
    for entry in journal_entries:
        st.write(entry)

    