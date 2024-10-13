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
    page = "Pages/Journal.py",
    title = "Journal",
    icon = ":material/book:",
)

home_page = st.Page(
    page = "Pages/Home.py",
    title = "Home",
    icon = ":material/nest_eco_leaf:",
    default= True,
)

Page_page = st.Page(
    page = "Pages/Page.py",
    title = "New Page",
    icon = ":material/note_add:"
)


Login_page = st.Page(
    page = "Pages/Login.py",
    title = "Log in"
)

Demo_page = st.Page(
    page = "Pages/Demo.py",
    title = "Demo",
    icon = ":material/play_arrow:",
)

# --- Navigation setup [without sections] --

st.logo("Assets/JADALOGO.png") 

NPG = st.navigation(pages=[about_page, journal_page, home_page, Page_page, Login_page, Demo_page])
NPG.run()






# st.markdown(
#         "<h1 style='text-align: center;'>WELCOME</h1>", 
#         unsafe_allow_html=True
# #     )
# image_path = "Assets/JADALOGO.png"
# with col2:
#     st.image(image_path, width=450)
    

# Logo_Image = Image.open("Assets/JADALOGO.png")
# st.image(
#     Logo_Image,
#     caption = "JADA is a Journaling AI Detection App. Anger, joy, sadness, write your mind down and see what JADA thinks",
#     width= 900,
#     #channels= "RGB"
# )


# Display and center the image


# markdown to create a container that centers the image
# st.markdown(
#     f"""
#     <div style="display: flex; justify-content: center;">
#         <img src="{image_path}" alt="centered image" width="300">
#     </div>
#     """,
#     unsafe_allow_html=True
# )
# Local image path

# Create two empty columns with one column in the center


# Center the image in the middle column


#st.image(image_path, width=800)
#st.text("J-A-D-A is a journaling AI Detection App. Anger, joy, sadness, write your mind down and see how jada interprets it.\n")
#st.markdown("![Hello](Assets/JADAAI.png)")
