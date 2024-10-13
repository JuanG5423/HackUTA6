import streamlit as st
import os
from cryptography.fernet import Fernet
from Pages.Login import get_auth_key

if st.session_state.user_state['logged_in']:
    key = get_auth_key()
        
    f = Fernet(key)
    def truncate_string(string, max_length):
        if len(string) <= max_length:
            return string
        else:
            return string[:max_length] + "..."

    col1, center, col3 = st.columns([2, 2, 2])
    with center:
        folder_path = './entries'
        for file_name in os.listdir(folder_path):
            # Check if the file has a .jada extension
            if file_name.endswith('.jada') and file_name.startswith(str(st.session_state.user_state['user_ID'])):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r') as file:
                    context = f.decrypt(file.read().encode('utf-8')).decode()
                    container = st.container(border=True)
                    container.columns(len(os.listdir(folder_path)), vertical_alignment="bottom")
                    container.write(truncate_string(context, 100))

        add_page = st.container()
        add_page.page_link("Pages/Page.py",label="Add Page",icon=":material/add_circle:")
        # if add_page.button("Add Page",icon=":material/add_circle:"):
        #     st.switch_page("Page.py")
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
    if st.button("OOPS! Need A Registered Account to use Journals.", icon=":material/warning:", key="OOPS"):
    # Toggle the button's state each time it's clicked
        st.session_state['button_active'] = not st.session_state['button_active']
        click(st.session_state['button_active'])
        
    
    


