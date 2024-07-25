from langchain_community.llms import Replicate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import Chroma
from prompt import get_prompt
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["REPLICATE_API_TOKEN"]=os.environ.get("REPLICATE_API_TOKEN")
class PDFChatbot():
    def __init__(self) -> None:
        self.llm = Replicate(
            model="meta/meta-llama-3-70b-instruct",
            input={"temperature": 0.75, "max_length": 3000}
            )
        self.db=None
        self.text_splitter=RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=200)
        self.embeddings=HuggingFaceEmbeddings()
        self.chain=None
        self.documents=None
        self.chat_history=[]
        self.prompt=get_prompt()
        
    def get_chunks(self,data):
        splits=self.text_splitter.split_text(data)
        return splits

    def get_vector_store(self,data_path):
        print("data path",data_path)
        if self.db is None:
            pdf_reader = PdfReader(data_path)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            self.documents=self.get_chunks(text)
            print("length of documents:",len(self.documents))
            self.db=Chroma.from_texts(self.documents,self.embeddings) 
            print("db is created")
            return self.db

    def get_response(self, query):
        similar_docs = self.db.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in similar_docs])
        formatted_prompt = self.prompt.format(context=context, query=query)
        result = self.llm.invoke(formatted_prompt)
        self.chat_history.append((query, result))
        return result  
    
        


