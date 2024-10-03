##Vishal -This is same code as simplerag.ipynb file,follow .ipynb file(jupiter  notebook) for better understanding.
##Vishal -This is my test file for the project .


## Data Ingestion
#from langchain_community.document_loaders import TextLoader
#loader=TextLoader("speech.txt")
#text_documents=loader.load()
#text_documents

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
# web based loader
#from langchain_community.document_loaders import WebBaseLoader
#import bs4

## load,chunk and index the content of the html page

#loader=WebBaseLoader(web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
 #                    bs_kwargs=dict(parse_only=bs4.SoupStrainer(
  #                       class_=("post-title","post-content","post-header")
#
 #                    )))

#text_documents=loader.load()

## Pdf reader
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('C:\\Users\\visha\\Documents\\Langchain\\Chatbot\\rag\\attention.pdf')
docs=loader.load()
#docs

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
documents=text_splitter.split_documents(docs)
documents[:5]

documents
## Vector Embedding And Vector Store
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(documents,OpenAIEmbeddings())

query = "Who are the authors of attention is all you need?"
retireved_results=db.similarity_search(query)
print(retireved_results[0].page_content)

## FAISS Vector Database
from langchain_community.vectorstores import FAISS
db1 = FAISS.from_documents(documents[:15], OpenAIEmbeddings())

##Vishal - Same above can be done using OLAMA to avoid the need for OPEN AI licence