import streamlit as st

def load_doc():
    document = st.file_uploader("", type=["pdf"])
    if document is not None:

        # Exibindo os detalhes
        file_details = {"filename":document.name}
        st.write(file_details)

def main():
    st.title('PDF CONVERTER')
    st.subheader('')
    st.subheader('Conversor pdf para o formato txt')
    st.subheader('')
    st.text('Arraste um arquivo pdf para realizar a conversão')
    load_doc()

if __name__ == "__main__":
    main()