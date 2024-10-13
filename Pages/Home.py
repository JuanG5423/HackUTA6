import streamlit as st
from PIL import Image


image_path1 = "Assets/JADALOGO.png"
col1, col2, col3 = st.columns([1,1,1])
col4, col5, col6 = st.columns([0.2, 1.5, 0.5])
top = st.container()
middle = st.container()
bottom = st.container()
              

with col5:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    image1 = st.image(image_path1, use_column_width=True);  # Full width for smaller screens
   
  
col4, col5, col6 = st.columns([0.2, 1.4, 0.5])

with bottom:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    with col5:
      with st.expander("Menu"):
            st.text("Create an Account or Login")
            st.page_link("Pages/Login.py", label= "Create or Login", icon=":material/login:")
            st.markdown("-------")
            
            st.text("How to Use")
            st.page_link("Pages/Demo.py", label= "Demo", icon=":material/play_arrow:")
            st.markdown("-------")
            
            st.text("Access Your Journal")
            st.page_link("Pages/Journal.py", label= "Journal", icon=":material/book:")
            st.markdown("-------")
            
            st.text("Know The Team")
            st.page_link("Pages/Aboutus.py", label= "The Team", icon=":material/groups:")
            
            
                      
st.text("")
image_path2 = "Assets/JADAAI.jpeg"
with bottom:
    with col6:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.image(image_path2, width=150);
   
# Render the image as a button
# st.markdown(
#     f"""
#     <a href="http://localhost:8501/Demo;" onclick="document.getElementById('image_button').click();">
#         <img src="Assets/JADAAI.jpeg" style="width: 200px; cursor: pointer;" />
#     </a>
#     """,
#     unsafe_allow_html=True
# )


    