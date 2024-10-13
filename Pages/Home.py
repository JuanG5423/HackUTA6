import streamlit as st
from PIL import Image

image_path1 = "Assets/JADALOGO.png"
image_path2 = "Assets/JADAAI.jpeg"
# with col2:
#     st.image(image_path, width=450)
col1, col2, col3 = st.columns([1, 2, 1])
top = st.container()
middle = st.container()
bottom = st.container()

with top:
    with col2:
    # Dynamically set image width based on perceived container width
        st.image(image_path1, use_column_width=True);  # Full width for smaller screens
   
   
    st.text(
    "JADA is a Journaling AI Detection App. Anger, joy, sadness, write your mind down and\nsee what JADA thinks"
    )


# button = col2.button("", icon= "Assets/JADAAI.png", use_container_width=True)

with bottom:
    if st.button("Try it out", icon= ":material/play_arrow:", help="Click me!"):
    # Add your button action here  
        st.markdown("[Demo](http://localhost:8501/Demo)", unsafe_allow_html=True)
    
    
        st.image(image_path2, width=100);

# Render the image as a button
# st.markdown(
#     f"""
#     <a href="http://localhost:8501/Demo;" onclick="document.getElementById('image_button').click();">
#         <img src="Assets/JADAAI.jpeg" style="width: 200px; cursor: pointer;" />
#     </a>
#     """,
#     unsafe_allow_html=True
# )


    