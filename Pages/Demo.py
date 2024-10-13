import streamlit as st
top = st.container()
middle = st.container()
bottom = st.container()



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
        # click(st.session_state['button_active'])
        
        
        


    