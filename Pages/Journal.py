import streamlit as st
import os
import pathlib
from cryptography.fernet import Fernet
from Pages.Login import get_auth_key, decrypt_journal
from ai import analyze_input
from transformers import pipeline


def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
        
css_path = pathlib.Path("Pages/style.css")
load_css(css_path)

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

                    @st.dialog("JADA is Responding...")
                    def AI_popUP(button_active):
                        dail_col1, dail_col2, dail_col3 = st.columns([1,2,1])
                        dail_top = st.container()
                        dail_center = st.container()
                        dail_bottom = st.container()
                        with dail_col1:
                            if button_active == True:
                                emotion, confidence = analyze_input(pipeline("text-classification", model="model", tokenizer="tokenizer"), context)
                                st.write(f"Your journal entry indicates that you are feeling {emotion} with {confidence}% confidence.")
                                if emotion == "suicidal":
                                    st.write("I'm so sorry you're feeling like that. Please reach out to a mental health professional or call the suicide hot line at 1-800-273-8255. Sometimes talking to someone close can help too! such as a friend or family memeber.")
                                elif emotion == "sexual violence" or emotion == "physical violence":
                                    st.write("It seems you're facing some serious issues, it is recommended to either contact the police or the domestic abuse hot line: 1−800−799−SAFE(7233)")                        
                        with dail_col3:
                            st.text("")
                            st.text("")
                            st.text("")
                            st.text("")
                            st.text("")
                            st.image("Assets/JADAAI.png", width=100)
        add_page = st.container()
        add_page.page_link("Pages/Page.py",label="Add Page",icon=":material/add_circle:")
        # if add_page.button("Add Page",icon=":material/add_circle:"):
        #     st.switch_page("Page.py")
        
        with col3:
            st.text("")
            st.text("")
            st.text("")
            st.text("") 
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            if 'button_active' not in st.session_state:
                    st.session_state['button_active'] = False

        # Create a button
            if st.button("", icon=":material/psychology_alt:", key="Help"):
            # Toggle the button's state each time it's clicked
                st.session_state['button_active'] = not st.session_state['button_active']
                AI_popUP(st.session_state['button_active'])
     
        
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

