# End to End GenAI Pretrained LLM model medical Chatbot Application with Custom PDF Data

# End-to-end-Medical-Chatbot-using-Llama2


https://github.com/user-attachments/assets/64f5ec83-112e-425a-a979-1b8670b19576



# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mchatbot python=3.8 -y
```

```bash
conda activate mchatbot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone



### Project Summary:
The Medical Chatbot using Generative AI leverages pre-trained language models and advanced document processing techniques to assist users with medical queries. It integrates document loading, text splitting, and embedding management with a retrieval-based question-answering system. Powered by Flask for a user-friendly interface, the chatbot retrieves relevant medical information from a Pinecone database, ensuring accurate and contextually relevant responses to user inquiries.

Here's an explanation of the core components of your medical chatbot project without delving into specific code details:

### Core Components of the Project

1. **Document Loading and Processing:**
   The project includes functionality to load medical documents, typically in PDF format. These documents contain unstructured text data that needs to be processed to extract meaningful information relevant to user queries.

2. **Text Splitting:**
   Once loaded, the documents are processed to split large chunks of text into smaller, manageable segments. This process ensures that the chatbot can handle and process specific sections of text efficiently during user interactions.

3. **Embeddings Download and Management:**
   To understand and generate meaningful responses, the project utilizes pre-trained vector embeddings from models like Hugging Face's Sentence Transformers. These embeddings convert text into numerical representations that capture semantic meanings, crucial for accurate response generation.

4. **Pinecone Integration for Vector Storage:**
   The project integrates with Pinecone, a cloud-based vector database. It stores and manages the embeddings generated from medical documents efficiently. This integration enables fast retrieval of relevant information based on user queries, enhancing the chatbot's responsiveness.

5. **Flask Application for User Interface:**
   The project employs Flask, a lightweight web framework in Python, to build a user-friendly interface for the chatbot. This interface allows users to interact with the chatbot via a web browser, inputting medical queries and receiving responses in a seamless manner.

6. **Prompt Generation and Language Model Interaction:**
   The chatbot utilizes a Prompt Template to structure user queries for the language model. This template ensures that the queries are formulated in a way that the pre-trained language model (LLM) can understand and generate accurate responses based on the embedded medical knowledge.

7. **Retrieval Question-Answering (QA) System:**
   A retrieval-based QA system is implemented to combine document retrieval with language model querying. This system retrieves relevant documents or responses from the Pinecone database based on user queries, ensuring that the chatbot provides contextually accurate answers.

8. **Environmental Configuration:**
   Configuration involves setting up environment variables securely, such as API keys for external services like Pinecone. This ensures that sensitive information is protected while enabling seamless integration and functionality of the chatbot.

### Summary
These core components work together to create a robust medical chatbot capable of understanding user queries, retrieving relevant medical information from stored documents, and generating accurate responses using advanced language modeling techniques. The integration of document processing, embeddings, retrieval systems, and a user-friendly interface via Flask forms the foundation of the project's functionality and usability.
