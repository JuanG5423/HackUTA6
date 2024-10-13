import streamlit as st 
import pathlib


def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
        
css_path = pathlib.Path("Pages/style.css")

col1, col2, col3 = st.columns(3)


nafi_IP = "Assets/nafidead.jpg"
juan_IP = "Assets/juandead.jpg"
abdul_IP = "Assets/jonjondead.jpg"


# Define function to display information after a button is clicked
def after_click(button_name):
    if button_name == "button1":
        st.subheader("NAFI")
        st.image(nafi_IP, use_column_width=True)
        st.text("Nafi worked on stuff")
    elif button_name == "button2":
        st.subheader("JUAN")
        st.image(juan_IP, use_column_width=True)
        st.text("Juan worked on AI stuff")
    elif button_name == "button3":
        st.subheader("JON JON")
        st.image(abdul_IP, use_column_width=True)
        st.text("Jon Jon worked on something")


# Top container section
top = st.container()
middle = st.container()
bottom = st.container()

# Check for button clicks using session state
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = None


# Check which button was clicked and update the session state
with top:
    st.title("Meet the Team")
    button1 = st.button("NAFI",icon=":material/sentiment_very_dissatisfied:", key="green")
    if button1:
        st.session_state['button_clicked'] = "button1"
        after_click(st.session_state['button_clicked'])
with middle:
    button2 = st.button("JUAN", icon=":material/stress_management:", key="red")
    if button2:
        st.session_state['button_clicked'] = "button2"
        after_click(st.session_state['button_clicked'])
with bottom:
    button3 = st.button("JON JON", icon=":material/sentiment_neutral:", key="black")
    if button3:
        st.session_state['button_clicked'] = "button3"
        after_click(st.session_state['button_clicked'])

    # Call after_click with the correct button name stored in session state

# def after_click():
#     if  button1:
#         st.subheader("NAFI")
#         st.image(nafi_IP, use_column_width=True)
#         st.text("Nafi worked on stuff")
#     elif button2:
#         st.subheader("JUAN")
#         st.image(juan_IP, use_column_width=True)
#         st.text("Juan worked on AI stuff")
#     elif button3:
#         st.subheader("JON JON")
#         st.image(abdul_IP, use_column_width=True)
#         st.text("Jon Jon worked on something")
        

# top = st.container() 
       
# with top:
#     st.title( "Meat the Team")
#     button1 = st.button("",icon=":material/sentiment_very_dissatisfied:", key="green")
#     if button1:
#         after_click()


# middle = st.container()
# with middle:
#     button2 = st.button("", icon=":material/stress_management:", key="red")
#     if button2:
#         after_click()
        
        
# bottom = st.container()     
# with bottom:
#     button3 = st.button("", icon=":material/sentiment_neutral:", key="black")
#     if button3:
#         after_click()
    
# st.html(
#         """
#         <head>
#             <title> Meat the Team</title>
#             <link rel="stylesheet" type = "text/css" href = "style.css">
            
#             <link rel= "preconnect" href="https://fonts.googleapis.com">
#             <link rel= "preconnect" href="https://fonts.gstatic.com" crossorigin>
#             <link href = "https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
#         </head>
#         <body>
#             <section class = "about">
#                 <div class = "main">
#                 <div class="about-text">
#                     <h1> About us</h1>
#                     <h5> Developer & Designer</h5>
#                     <p>I am Abdulmuizz Wahab and I mostly worked on the styling with the front end of our APP.</p>
#         """
#         )