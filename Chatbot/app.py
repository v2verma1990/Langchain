from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
##Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
## Promt Template

promt=ChatPromptTemplate.from_messages(
[
    ("system","you are a helpful assistant.Please respond to the queries"),
    ("user","Question:{question}")
]
)

##streamlit framework

st.title="ChatDemo with OpenAI"
input_text=st.text("Search the topic you want")

##call openai LLM  
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()

chain=promt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

