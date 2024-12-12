
# Information Retrieval System - PDF

This Streamlit application allows users to upload PDF documents, ask questions about their content, and receive relevant answers. It leverages LangChain, Google Generative AI, and FAISS to create a conversational interface for information retrieval.
![image](https://github.com/user-attachments/assets/25aca6c0-fa98-4226-9683-522b9f06e441)

**Features:**

- **PDF Upload:** Upload multiple PDF files directly within the application.
- **Vector Store Creation:** The application automatically creates a vector store from the uploaded PDF content using Google Generative AI embeddings and FAISS.
- **Conversational Interface:** Interact with the system by asking questions about the uploaded PDF documents. The application will provide relevant answers based on the vector store.
- **Chat History:** The conversation history is maintained and displayed for easy reference.

**Installation:**

1. **Install required libraries:**
- Dependencies:
- streamlit
- langchain
- PyPDF2
- google-api-python-client
- faiss

2. **Setup:**
- Obtain necessary API keys/credentials:
- Google Cloud AI Platform credentials for accessing Google Generative AI.
- Configure the application with the required credentials.

 3. **Run the Application:**
Execute the main script (e.g., streamlit run app.py).

 4. **Usage:**
- Upload PDF files within the Streamlit interface.
- Ask questions related to the content of the uploaded PDFs.
- Review the conversation history.

5.**Testing Results:**
![image](https://github.com/user-attachments/assets/e97ed961-806a-4671-8d5b-92e9769318a9)


This Readme file provides a basic framework. You can customize it further to better suit your project's specific needs and audience.
