import streamlit as st 
import pathlib


def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
        
css_path = pathlib.Path("Pages/style.css")
load_css(css_path)

col1, col2, col3 = st.columns([2,4,2])


nafi_IP = "Assets/nafidead.jpg"
juan_IP = "Assets/juandead.jpg"
abdul_IP = "Assets/jonjondead.jpg"


# Define function to display information after a button is clicked
# Everyone should describe their contribution level and what they exactly did on the project
def after_click(button_name):
    if button_name == "button1":
        st.subheader("NAFI")
        st.image(nafi_IP, use_column_width=True)
        with st.expander("What he do?"):
            st.markdown("----------");
            st.text("I created the Page system for the journal as well as the \nLogin system for the app to ensure that only registered users are allowed \nto use the program.\n(I also spent my last brain cell holding my will to live and will be\nusing this program extensivly after Hack...)")
    elif button_name == "button2":
        st.subheader("JUAN")
        st.image(juan_IP, use_column_width=True)
        with st.expander("What he do?"):
            st.markdown("----------")
            st.text("Trained the emotion detection model\nand by train I mean waited like 10 hours for it to finish.")
    elif button_name == "button3":
        st.subheader("JON JON")
        st.image(abdul_IP, use_column_width=True)
        with st.expander("What he do?"):
            st.markdown("----------")
            st.markdown("""
                        - Did not want to do the project
                        - Ended up joining a side quest of doing a project
                        - Ended up being broke on points
                        - Ended up doing streamlit library functionality with entegrated custom HTML, CSS handling
                        - Ended up up doing button handling streamlit style ( very very fun )
                        """)
            


# Top container section
top = st.container()
middle = st.container()
bottom = st.container()

# Check for button clicks using session state
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = None


    # Create the buttons


# Check which button was clicked and update the session state

with top:
    st.title("Meet the Team")
    button1 = st.button("NAFI", icon=":material/sentiment_very_dissatisfied:", key="NAFI")
    if button1:
        st.session_state['button_clicked'] = "button1"
        after_click(st.session_state['button_clicked'])
with middle:
    button2 = st.button("JUAN",icon=":material/stress_management:", key="JUAN")
    if button2:
        st.session_state['button_clicked'] = "button2"
        after_click(st.session_state['button_clicked'])
with bottom:
    button3 = st.button("JON JON",icon=":material/sentiment_neutral:", key="JONJON")
    if button3:
        st.session_state['button_clicked'] = "button3"
        after_click(st.session_state['button_clicked'])
        
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    
    # - Shout out to our sponsors
    st.title("Shotout to a few Sponsors")
    with st.expander("Sponsors"):
        st.image("Assets/MouseE.png", caption="Mouser Electronics", width=150)
        st.image("Assets/MLH.png", caption="Major League Hacking", width=150)
        st.image("Assets/FA.png", caption="Founders Arena", width=150)
        st.image("Assets/utalogo.png", caption="Computer Science and Engineering", width=150)
        st.image("Assets/utalogo.png", caption="Information Security Officer", width=150)
        st.image("Assets/utalogo.png", caption="UTA Libraries", width=150)
        
    
      
with st.expander("Menu"):
    st.text("Create an Account or Login")
    st.page_link("Pages/Login.py", label= "Create or Login", icon=":material/login:")
    st.markdown("-------")
            
    st.text("How to Use")
    st.page_link("Pages/Demo.py", label= "Demo", icon=":material/play_arrow:")
    st.markdown("-------")
              
    st.text("Know The Team")
    st.page_link("Pages/Aboutus.py", label= "The Team", icon=":material/groups:")
        


    