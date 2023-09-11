def main():
    load_dotenv()
    st.set_page_config(page_title="Pullm-AI, Repositorio Inteligente", page_icon=":robot_face:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Create columns for layout adjustment
    left_column, right_column = st.beta_columns([1, 3])

    with right_column:
        st.header("Asistente Virtual para consultas sobre Procedimientos")

        # This will allow for scrolling and encapsulate the chat in its container
        with st.beta_container():
            if st.session_state.chat_history:
                for i, message in enumerate(st.session_state.chat_history):
                    if i % 2 == 0:
                        st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
                    else:
                        st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

    with left_column:
        st.subheader("Documentos")
        pdf_docs = st.file_uploader("Cargar archivos PDF y apretar 'Procesar'", accept_multiple_files=True)
        if st.button("Procesar"):
            with st.spinner("Procesando"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

    # Set the user input bar at the bottom
    user_question = st.text_input("Consultar sobre procedimientos")
    if user_question:
        handle_userinput(user_question)

if __name__ == '__main__':
    main()
