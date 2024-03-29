import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()
llm=OpenAI(model='gpt-3.5-turbo-instruct',temperature=0.9, max_tokens=500)
st.title("News Research Tool")
st.sidebar.title("News Article URLs")

urls=[]
for i in range(3):
    url=st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked= st.sidebar.button("Process URL")
file_path='vectorestore.pkl'

main_placefolder= st.empty()
if process_url_clicked:
    #load data
    loader=UnstructuredURLLoader(urls=urls)
    data=loader.load()

    main_placefolder.text("Processing")

    #Split data
    text_splitter=RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size=1000
    )
    docs=text_splitter.split_documents(data)

    #create embeddings

    embeddings=OpenAIEmbeddings()
    vectorstore=FAISS.from_documents(docs,embeddings)

    #save the vector as a pickle file

    with open(file_path,'wb') as f:
        pickle.dump(vectorstore,f)

query = main_placefolder.text_input("Question: ")

if query:
    if os.path.exists(file_path):
        with open(file_path,"rb") as f:
            vectors=pickle.load(f)
            chain=RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectors.as_retriever())
            result=chain({"question":query},return_only_outputs=True)
            st.header("Answer")
            st.write(result['answer'])

            sources=result.get("sources:")
            if sources:
                st.subheader("Sources:")
                sources_list=sources.split("\n")
                for source in sources_list[:5]:
                    st.write(source)