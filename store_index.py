
from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os
from langchain.vectorstores import Pinecone as PineconeStore

load_dotenv()

# fetching the unique api key and index name of pine cone which helps us to save the embedded dense vector in this pinecone vector database
import os 
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')  # API Key value which i saved in .env for security purpose and fetching the key value name here through os.getenv, so we can prevint the pinecone api key to display in public
PINECONE_API_index_env='test' # api index name which we need to create for storing the vectors in pinecone database, In order to store this each vector embedding which consist of 384 dense vector embedding into pinecone database while the time of creating the index in the pincone we need to give the dense vector embedding dimension as 384 according to pretrained vector embedding model dimension and give metrics as cosine for calculating the distance between the among each vectors while helps us to find the semantic relationship between 2 sentences 

# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


# Initializing the Pinecone database
# Creating Embeddings for Each of The Text Chunks & storing
docsearch = PineconeStore.from_texts([t.page_content for t in text_chunks],embeddings, index_name=PINECONE_API_index_env)  # here i pass the 7020 small indiviual documents chunks or small paragraphs which each documents consist of 500 tokens + 20 previous document tokens and these each document passing to the model for converting the each individual  document chunk into dense vector embedding by pretraiend vector embedding model from huggingface (which i passed in the name of embeddings) and with the help of index name we passed which is test which help us to do this task at the same time store those all each dense vector embdding in pinecone vector database 
