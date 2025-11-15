import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory

# PDF 처리 함수
@st.cache_resource
def process_pdf():
    loader = PyPDFLoader('../data/2024_KB_부동산_보고서_최종.pdf')
    documents = loader.load()
    text_splitter = SemanticChunker(embeddings=OpenAIEmbeddings())
    chunks = text_splitter.split_documents(documents)
    
    return chunks

# 벡터 저장소 초기화
@st.cache_resource
def initialize_vectordb():
    chunks = process_pdf()
    vectordb = Chroma.from_documents(documents=chunks, embedding=OpenAIEmbeddings(), persist_directory='./chroma')

    return vectordb

# 체인 초기화
@st.cache_resource
def initialize_chain():
    vectordb = initialize_vectordb()
    retriever = vectordb.as_retriever(search_kwargs={'k':3})

    template = '''당신은 KB 부동산 보고서 전문가입니다. 다음 정보를 바탕으로 사용자의 질문에 답변해주세요.
    
    컨텍스트: {context}'''

    prompt = ChatPromptTemplate.from_messages(
        [('system', template),
         ('placeholder', '{chat_history}'),
         ('human', '{question}')]
    )

    model = ChatOpenAI(model='gpt-5-nano', temperature=0)

    def format_docs(docs):
        return '\n\n'.join(doc.page_content for doc in docs)
    
    base_chain = (
        RunnablePassthrough.assign(context=lambda x: format_docs(retriever.invoke(x['question'])))
        | prompt
        | model
        | StrOutputParser()
    )

    chain_with_history = RunnableWithMessageHistory(
        base_chain,
        lambda session_id: ChatMessageHistory(),
        input_messages_key='question',
        history_messages_key='chat_history'
    )

    return chain_with_history

# Streamlit UI
def main():
    st.set_page_config(page_title='KB 부동산 보고서 챗봇', page_icon='🏠')
    st.title('🏠 KB 부동산 보고서 AI 어드바이저')
    st.caption('2024 KB 부동산 보고서 기반 질의응답 시스템')

    # 세션 상태 초기화
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # 채팅 기록 표시
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    
    # 사용자 입력 처리
    if prompt := st.chat_input('부동산 관련 질문을 입력하세요.'):
        # 사용자 메시지 표시
        with st.chat_message('user'):
            st.markdown(prompt)
        st.session_state.messages.append({'role':'user', 'content':prompt})

        # 체인 초기화
        chain = initialize_chain()

        # AI 응답 생성
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
