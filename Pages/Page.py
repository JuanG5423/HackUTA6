import streamlit as st
from cryptography.fernet import Fernet
from Pages.Login import get_auth_key
import datetime
import os
import pathlib

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
        
css_path = pathlib.Path("Pages/style.css")
load_css(css_path)

if st.session_state.user_state['logged_in']:

    # Fetch the encryption key from the user's session state
    key = get_auth_key()
    f = Fernet(key)
    time_stamp = datetime.datetime.now()

    # Get the user ID from session state and build the file path
    user_id = str(st.session_state.user_state['user_ID'])
    file_path = f"entries/{user_id}entry{time_stamp.strftime('%d%m%Y%M')}.jada"

    st.title("How Are You Feeling Today?")
    entry = st.text_area("Write your feelings", height=900)

    # Prepare the content to be written
    if entry:
        # Check if the file already exists
        if os.path.exists(file_path):
            # Read existing encrypted content from the file
            with open(file_path, 'r') as file:
                existing_encrypted_content = file.read()

            # Decrypt the existing content
            try:
                existing_content = f.decrypt(existing_encrypted_content.encode('utf-8')).decode('utf-8')
            except Exception as e:
                st.error("Error decrypting the existing content. Please ensure the file is valid.")
                existing_content = ""

            # Combine the existing content with the new entry
            combined_content = existing_content + "\n" + entry
        else:
            # If the file doesn't exist, just use the new entry
            combined_content = entry

        # Encrypt the combined content
        encrypted_content = f.encrypt(combined_content.encode('utf-8')).decode('utf-8')

        # Write the encrypted content back to the file
        with open(file_path, 'w') as file:
            file.write(encrypted_content)
            file.write("\n")

        st.success("Your entry has been saved.")
else:
    def click(button_active):
        if button_active == True:
            with st.expander("Options"):
                st.page_link("Pages/Login.py", label= "Create or Login", icon=":material/login:")
                st.markdown("-------")
                st.page_link("Pages/Home.py", label="Home", icon=":material/nest_eco_leaf:")
                
    
    if 'button_active' not in st.session_state:
        st.session_state['button_active'] = False

    # Create a button
    if st.button("OOPS! Need A Registered Account to add a Page.", icon=":material/warning:", key="OOPS"):
    # Toggle the button's state each time it's clicked
        st.session_state['button_active'] = not st.session_state['button_active']
        click(st.session_state['button_active'])

