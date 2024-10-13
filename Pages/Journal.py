import streamlit as st
import os
import pathlib
from cryptography.fernet import Fernet
from Pages.Login import get_auth_key, decrypt_journal
from ai import analyze_input
from transformers import pipeline


# Load custom CSS for styling
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("Pages/style.css")
load_css(css_path)

if st.session_state.user_state['logged_in']:
    key = get_auth_key()
    f = Fernet(key)

    # Truncate the string to a specific length
    def truncate_string(string, max_length):
        if len(string) <= max_length:
            return string
        else:
            return string[:max_length] + "..."

    folder_path = './entries'
    files = [f for f in os.listdir(folder_path) if f.endswith('.jada') and f.startswith(str(st.session_state.user_state['user_ID']))]

    # Dialog to show results after analysis
    @st.dialog("JADA is Responding...")
    def analyze_file(context):
        emotion, confidence = analyze_input(pipeline("text-classification", model="model", tokenizer="tokenizer"), context)
        output = f"Your journal entry indicates that you are feeling {emotion} with {confidence}% confidence." if emotion == "suicidal" else f"Your journal entry indicates that you are experiencing {emotion} with {confidence}% confidence."
        st.write(output)
        if emotion == "suicidal":
            st.write("I'm so sorry you're feeling like that. Please reach out to a mental health professional or call the suicide hotline at 1-800-273-8255. Sometimes talking to someone close can help too, such as a friend or family member.")
        elif emotion in ["sexual violence", "physical violence"]:
            st.write("It seems you're facing some serious issues. It is recommended to either contact the police or the domestic abuse hotline: 1-800-799-SAFE (7233).")

    # Display each journal file with its content and an "Analyze" button to the right
    if files:  # Check if there are any files before displaying
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                context = f.decrypt(file.read().encode('utf-8')).decode()
                truncated_text = truncate_string(context, 100)

                # Create columns for layout: file content in one column, button in another column
                col1, col2 = st.columns([4, 1])

                with col1:
                    # Box the journal content with some padding and border
                    st.markdown(f"""
                    <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
                        {truncated_text}
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    # Place the analyze button in the second column (to the right)
                    if st.button(f"Ask JADA", key=f"Analyze_{file_name}"):
                        analyze_file(context)

        # Center the "Analyze All Entries" button if files exist
        if files:  # Show button only if there are entries
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("Analyze All Entries"):
                    all_text = ""
                    for file_name in files:
                        file_path = os.path.join(folder_path, file_name)
                        with open(file_path, 'r') as file:
                            all_text += f.decrypt(file.read().encode('utf-8')).decode() + "\n"
                    analyze_file(all_text)
    else:
        st.write("No journal entries found.")

else:
    def click(button_active):
        if button_active:
            with st.expander("Options"):
                st.page_link("Pages/Login.py", label="Create or Login", icon=":material/login:")
                st.markdown("-------")
                st.page_link("Pages/Home.py", label="Home", icon=":material/nest_eco_leaf:")

    if 'button_active' not in st.session_state:
        st.session_state['button_active'] = False

    if st.button("OOPS! Need A Registered Account to use Journals.", icon=":material/warning:", key="OOPS"):
        st.session_state['button_active'] = not st.session_state['button_active']
        click(st.session_state['button_active'])
