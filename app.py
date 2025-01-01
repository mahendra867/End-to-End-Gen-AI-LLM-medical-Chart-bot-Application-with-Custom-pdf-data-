from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone as PineconeStore
from langchain import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace

from huggingface_hub import login



app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')  # API Key value which i saved in .env for security purpose and fetching the key value name here through os.getenv, so we can prevint the pinecone api key to display in public
PINECONE_API_index_env='test' # api index name which we need to create for storing the vectors in pinecone database, In order to store this each vector embedding which consist of 384 dense vector embedding into pinecone database while the time of creating the index in the pincone we need to give the dense vector embedding dimension as 384 according to pretrained vector embedding model dimension and give metrics as cosine for calculating the distance between the among each vectors while helps us to find the semantic relationship between 2 sentences 



embeddings = download_hugging_face_embeddings()



#Loading the existing index
# If we already have an index which it consist of dense vector embeddings of documents (chunks) we can load it like this
docsearch=PineconeStore.from_existing_index(PINECONE_API_index_env, embeddings)


# Create the PromptTemplate object
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context","question"])

# Define chain_type_kwargs using the created PROMPT
chain_type_kwargs = {"prompt": PROMPT}

#llm=CTransformers(model="meta-llama/Llama-3.2-1B", # with the help of CTransformers we can able to load the  llama llm model by giving some customize paramerters for the llm model
#                  model_type="llama",
#                  config={'max_new_tokens':512,
#                          'temperature':0.8})




groq_api_key=os.getenv('GROQ_API_KEY')
llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama3-8b-8192")

# here i have created the object for the RetrievalQA.from_chain_type and given object name as qa
qa=RetrievalQA.from_chain_type(
    llm=llm,  # passed the llama llm
    chain_type="stuff",  # The "stuff" chain type is useful because it simplifies the process of combining document retrieval with language model querying. It ensures that the language model has access to the returned documents which gives the most relevant information when generating a response to the users query This is particularly important in scenarios where the model needs to provide accurate and contextually relevant answers, such as in question-answering systems or chatbots.
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),  # here passed the docsearch which is knowledge base which it consist of vecttor embeddings of all documents and it return best 2 documents or 2 relevant answers w.r.t user qeury and passed it to the retriver variable and our llama llm model gives the correct refine response to user query by refining the 2 documents answers 
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)