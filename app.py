import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

# Set page configuration
st.set_page_config(page_title="Information Retrieval System - Sathish", page_icon="📚", layout="wide")

# Add custom CSS for styling
st.markdown("""
    <style>
        .main-container {
            background-color: #ADD8E6; /* Light blue background */ 
            padding: 15px;
            border-radius: 5px;
        }
        .st-by {
            text-align: side;
            font-style: italic;
            margin-top: 20px;
        }
        .st-by1 {
            text-align: center;
            font-style: italic;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

def user_input(user_question):
    """
    Handles user input and displays the conversation history.

    Args:
        user_question: The question entered by the user.
    """
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write("**User:**", message.content)
        else:
            st.write("**Reply:**", message.content)

def main():
    """
    Main function to execute the Streamlit application.
    """
    # Display logo and title
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://images.miraclesoft.com/miracle-logo-dark.svg", width=150)  # Replace with your company logo path
    with col2:
        st.title("Information Retrieval System - PDF")

    # Initialize session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None

    # Create a single column for the main content
    st.markdown("<div class='main-container'>", unsafe_allow_html=True) 
    user_question = st.text_input("Ask a Question from the PDF Files", key="user_question")
    if user_question:
        user_input(user_question)
    st.markdown("</div>", unsafe_allow_html=True) 

    # Sidebar
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    try:
                        raw_text = get_pdf_text(pdf_docs)
                        text_chunks = get_text_chunks(raw_text)
                        vector_store = get_vector_store(text_chunks)
                        st.session_state.conversation = get_conversational_chain(vector_store)
                        st.success("Done! You can now ask questions.")
                        st.session_state.chatHistory = []
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
            else:
                st.warning("Please upload PDF files first.")

    # Display "Developed by" with your name
    st.markdown("<div class='st-by1'>Developed by: Sathish Mattapalli</div>", unsafe_allow_html=True) 


if __name__ == "__main__":
    import os
    import subprocess

    # Get the port from the environment variable, default to 8080
    port = int(os.environ.get("PORT", 8080))

    # Ensure compatibility with deployment environments
    script_path = os.path.abspath(__file__)
    subprocess.run(["streamlit", "run", script_path, "--server.port", str(port)])
    main()