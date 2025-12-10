import os
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import ChatOpenAI
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

model = ChatOpenAI(model='gpt-5-mini', temperature=0)
embeddings = HuggingFaceEmbeddings(model='BAAI/bge-m3', model_kwargs={'device':'cuda'}, encode_kwargs={'batch_size':8})

def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)

@st.cache_resource
def process_pdf():
    loader = PyPDFLoader('../data/2024_KB_부동산_보고서_최종.pdf')
    docs = loader.load()
    full_text = format_docs(docs)
    text_splitter = SemanticChunker(embeddings=embeddings)
    docs = text_splitter.create_documents([full_text])
    for doc in docs:
        doc.metadata['source'] = '2024_KB_부동산_보고서_최종.pdf'
    
    return docs

@st.cache_resource
def initialize_vectorstore():
    docs = process_pdf()

    return Chroma.from_documents(documents=docs, embedding=embeddings)

@st.cache_resource
def initialize_chain():
    vectorstore = initialize_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={'k':3})

    template = '''
    당신은 KB 부동산 보고서 전문가입니다. 다음 정보를 바탕으로 사용자의 질문에 답변해주세요.
    정보에 없는 내용은 "정보가 없어 답변할 수 없습니다." 라고 답변해주세요.
    컨텍스트: {context}
    '''
    prompt = ChatPromptTemplate.from_messages(
        [('system', template),
         ('placeholder', '{chat_history}'),
         ('human', '{question}')]
    )

    base_chain = (
        RunnablePassthrough.assign(context=lambda x: format_docs(retriever.invoke(x['question'])))
        | prompt
        | model
        | StrOutputParser()
    )
    chain_with_memory = RunnableWithMessageHistory(
        base_chain,
        lambda session_id: ChatMessageHistory(),
        input_messages_key='question',
        history_messages_key='chat_history'
    )

    return chain_with_memory

def main():
    st.set_page_config(page_title='KB 부동산 보고서 챗봇', page_icon='🏠')
    st.title('🏠 KB 부동산 보고서 AI 어드바이저')
    st.caption('2024 KB 부동산 보고서 기반 질의응답 시스템')

    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    
    if prompt := st.chat_input('부동산 관련 질문을 입력하세요.'):
        with st.chat_message('user'):
            st.markdown(prompt)
        st.session_state.messages.append({'role':'user', 'content':prompt})

        chain = initialize_chain()

        with st.chat_message('assistant'):
            with st.spinner('답변 생성 중..'):
                response = chain.invoke(
                    {'question':prompt},
                    {'configurable':{'session_id':'streamlit_session'}}
                )
                st.markdown(response)
        
        st.session_state.messages.append({'role':'assistant', 'content':response})

if __name__ == '__main__':
    main()