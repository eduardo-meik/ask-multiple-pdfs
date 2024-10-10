import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(model_name='gpt-4')
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory      
    )
    return conversation_chain

def handle_userinput(user_question):
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']
    else:
        st.warning("Por favor, carga y procesa documentos antes de iniciar la conversación.")

def display_chat_history():
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Pullm-AI, Repositorio Inteligente",
                       page_icon=":robot_face:", layout='wide')
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.header("Asistente Virtual para Gestión de Conocimiento")

    # Contenedor del chat
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Entrada de chat (Input bar on top)
    st.markdown('<div class="chat-input">', unsafe_allow_html=True)
    user_question = st.text_input("Escribe tu pregunta aquí...", key="input")
    st.markdown('</div>', unsafe_allow_html=True)  # Fin de la entrada de chat

    # Historial de chat
    st.markdown('<div class="chat-history">', unsafe_allow_html=True)
    if st.session_state.chat_history:
        display_chat_history()
    st.markdown('</div>', unsafe_allow_html=True)  # Fin del historial de chat

    st.markdown('</div>', unsafe_allow_html=True)  # Fin del contenedor del chat

    # Manejar entrada del usuario
    if user_question:
        handle_userinput(user_question)
        st.session_state.input = ""  # Limpiar el campo de entrada
        st.experimental_rerun()  # Refrescar la aplicación para mostrar el nuevo mensaje

    st.write("⚠️ **Atención:** Este chat puede proporcionar datos imprecisos. Requiere entrenamiento específico para un uso en particular. Siempre verifique la información antes de tomar decisiones basadas en ella.")

    with st.sidebar:
        st.subheader("Documentos")
        pdf_docs = st.file_uploader(
            "Cargar archivos PDF y presionar 'Procesar'", accept_multiple_files=True)
        if st.button("Procesar"):
            if pdf_docs:
                with st.spinner("Procesando..."):
                    # Obtener texto de los PDFs
                    raw_text = get_pdf_text(pdf_docs)

                    # Dividir el texto en fragmentos
                    text_chunks = get_text_chunks(raw_text)

                    # Crear el almacén vectorial
                    vectorstore = get_vectorstore(text_chunks)

                    # Crear la cadena de conversación
                    st.session_state.conversation = get_conversation_chain(
                        vectorstore)
                st.success("Documentos procesados exitosamente.")
            else:
                st.warning("Por favor, carga al menos un documento PDF.")

if __name__ == '__main__':
    main()
