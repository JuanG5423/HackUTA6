#import streamlit as st
import os
#from cryptography.fernet import Fernet
#from Pages.Login import get_auth_key

def analyze_entries(entries_directory):
    entries = []
    for file_name in os.listdir(entries_directory):
        if file_name.endswith('.jada'):
            with open(os.path.join(entries_directory, file_name), 'r') as file:
                entries.append(file.read()[:-1])
    #pipeline("text-classification", model="model", tokenizer="tokenizer")
    return entries

if __name__ == "__main__":


    # if st.session_state.user_state['logged_in']:
    #     key = get_auth_key()
            
    #     f = Fernet(key)
    #     def truncate_string(string, max_length):
    #         if len(string) <= max_length:
    #             return string
    #         else:
    #             return string[:max_length] + "..."

    #     col1, center, col3 = st.columns([2, 2, 2])
    #     with center:
    #         folder_path = './entries'
    #         for file_name in os.listdir(folder_path):
    #             # Check if the file has a .jada extension
    #             if file_name.endswith('.jada') and file_name.startswith(str(st.session_state.user_state['user_ID'])):
    #                 file_path = os.path.join(folder_path, file_name)
    #                 with open(file_path, 'r') as file:
    #                     context = f.decrypt(file.read().encode('utf-8')).decode()
    #                     container = st.container(border=True)
    #                     container.columns(len(os.listdir(folder_path)), vertical_alignment="bottom")
    #                     container.write(truncate_string(context, 100))

    #         add_page = st.container()
    #         add_page.page_link("Pages/Page.py",label="Add Page",icon=":material/add_circle:")
    #         # if add_page.button("Add Page",icon=":material/add_circle:"):
    #         #     st.switch_page("Page.py")
    # else:
    #     st.title("Login to use our App!!")
    
    print(analyze_entries('./entries'))
