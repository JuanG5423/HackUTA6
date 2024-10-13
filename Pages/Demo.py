import streamlit as st
import pathlib





top = st.container()
middle = st.container()
bottom = st.container()


def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
        
css_path = pathlib.Path("Pages/style.css")
load_css(css_path)

def click(button_active):
    if button_active == True: 
        video_file = open('demo_compressed.mp4', 'rb')
        video_bytes = video_file.read()
        
        st.video(video_bytes)
        
    
        

with top:
    st.title("Learning Guide")
    with st.expander("What is JADA?"):
        st.text(
            "JADA is a Journaling AI Detection App.\nAnger, joy, sadness, write your mind down\nand see what JADA thinks"
        )
        if 'button_active' not in st.session_state:
            st.session_state['button_active'] = False

# Create a button
        if st.button("Video", icon=":material/sentiment_satisfied:", key='Jada'):
    # Toggle the button's state each time it's clicked
            st.session_state['button_active'] = not st.session_state['button_active']
        click(st.session_state['button_active'])
        

    with st.expander("Menu"):
        st.text("Create an Account or Login")
        st.page_link("Pages/Login.py", label= "Create or Login", icon=":material/login:")
        st.markdown("-------")
            
        st.text("Home")
        st.page_link("Pages/Home.py", label= "Home", icon=":material/nest_eco_leaf:")
        st.markdown("-------")
              
        st.text("Know The Team")
        st.page_link("Pages/Aboutus.py", label= "The Team", icon=":material/groups:")
            
        
        
        


    