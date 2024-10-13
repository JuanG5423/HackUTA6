import streamlit as st 
from PIL import Image 


# -- Page setup -- 
# st.set_page_config(
#     page_title= "JADA APP",
#     page_icon= "JADAAI.png",
# )# Create user_state
if 'user_state' not in st.session_state:
    st.session_state.user_state = {
        'name_surname': '',
        'password': '',
        'logged_in': False,
        'user_type': '',
        'mail_adress': '',
        'auth_key': '',
        'user_ID': ''
    }

about_page = st.Page(
    page ="Pages/Aboutus.py",
    title="About us",
    icon =":material/groups:",
   
)

journal_page = st.Page(
    page = "Pages/Journals.py",
    title = "Journals",
    icon = ":material/book:",
)

home_page = st.Page(
    page = "Pages/Home.py",
    title = "Home",
    icon = ":material/nest_eco_leaf:",
    default= True,
)

Demo_page = st.Page(
    page = "Pages/Demo.py",
    title = "Demo",
    icon = ":material/play_arrow:",
)

Login_page = st.Page(
    page = "Pages/Login.py",
    title = "Login",
    icon=":material/login:"
)


# --- Navigation setup [without sections] --

st.logo("/home/unknown/HackUTA6/Assets/JADALOGO.png") 
NPG = st.navigation(pages=[about_page, journal_page, home_page, Demo_page])
NPG.run()




# st.markdown(
