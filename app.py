# PDF_CONVERTER
#
# Desenvolvido por César Calafrioli
#
import streamlit as st
from PyPDF2 import PdfFileReader

# Converter o arquivo pdf em formato txt
def conv_doc(file):
    
    pdfFile = open(file, "rb")

    # Criando o objeto do arquivo pdf
    pdfReader = PdfFileReader(pdfFile)

    # Recebendo o número de páginas
    count = pdfReader.numPages

    # Convertendo o arquivo PDF para o formato TXT
    for i in range(0+1, count):
        pageObj = pdfReader.getPage(i)
        text = pageObj.extractText()
        textFile = open(r"./teste.txt","a",encoding="utf-16")
        textFile.writelines(text)

        # Exibindo o progresso da conversão
        #latest_iteration.text(f'Convertendo {math.ceil((float(float(i)+1)/floaat(numPages))*100)} %')
        
    pdfFile.close()

    st.write(count)


# Ler o arquivo pdf
def load_doc():
    document = st.file_uploader("", type=["pdf"])
    if document is not None:

        # Exibindo os detalhes
        file_details = {"filename":document.name}
        st.write(file_details)

        # Botão para converter o arquivo PDF
        btnConv = st.button('Converter para TXT')
        
        # Converte o arquivo para TXT após o usuário clicar no botão
        if btnConv:
            with open(document.name,"wb") as f:
                f.write(document.getbuffer())
            conv_doc(document.name)

def main():
    st.title('PDF CONVERTER')
    st.subheader('')
    st.subheader('Conversor pdf para o formato txt')
    st.subheader('')
    st.text('Arraste um arquivo pdf para realizar a conversão')
    load_doc()

if __name__ == "__main__":
    main()