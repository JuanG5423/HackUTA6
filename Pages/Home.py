import streamlit as st
from PIL import Image

image_path = "Assets/JADALOGO.png"
# with col2:
#     st.image(image_path, width=450)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Dynamically set image width based on perceived container width
    st.image(image_path, use_column_width=True);  # Full width for smaller screens
   
   
st.text(
    "JADA is a Journaling AI Detection App. Anger, joy, sadness, write your mind down and\nsee what JADA thinks"
    )

    