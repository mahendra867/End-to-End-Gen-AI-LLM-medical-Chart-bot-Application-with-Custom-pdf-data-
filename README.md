# End to End GenAI Pretrained LLM model medical Chatbot Application with Custom PDF Data

## End-to-End Medical Chatbot using Llama2

### How to Run?

#### Steps:

1. **Clone the repository:**
git clone https://github.com/mahendra867/End-to-End-Gen-AI-LLM-medical-Chart-bot-Application-with-Custom-pdf-data-.git


2. **Create a Conda environment:**

conda create -n mchatbot python=3.8 -y
conda activate mchatbot


3. **Install the requirements:**

pip install -r requirements.txt



4. **Set up Pinecone credentials:**
- Create a `.env` file in the root directory.
- Add your Pinecone credentials:
  ```
  PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ```

5. **Download the quantized model:**
- Download the Llama 2 Model (`llama-2-7b-chat.ggmlv3.q4_0.bin`) from the following link:
  [Llama 2 Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
- Place the downloaded model file in the `model` directory of the project.

6. **Store the index:**


python store_index.py



7. **Run the application:**


python app.py


8. **Access the application:**
Open your web browser and go to `localhost`.

### Tech Stack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone


