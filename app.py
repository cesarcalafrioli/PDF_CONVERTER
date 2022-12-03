import streamlit as st
import platform
import subprocess
import os
import shutil

#  install the new version
# !wget --no-check-certificate https://dl.xpdfreader.com/xpdf-tools-linux-4.04.tar.gz
# !tar -xvf xpdf-tools-linux-4.04.tar.gz && sudo cp xpdf-tools-linux-4.04/bin64/pdftotext /usr/local/bin

# Diretórios onde ficarão armazenados os arquivos PDF e TXT
PDF_FOLDER = "files\\pdf"
TXT_FOLDER = "files\\txt"

# Converte o arquivo pdf para o formato txt.
# Detecta em qual sistema operacional o script está rodando
def conv_file(path, filename, sist_op):

    # Onde vai ficar o arquivo txt
    target_text_filename = filename.replace(".pdf",".txt")
    target_text_path = os.path.join(TXT_FOLDER, target_text_filename)

    # Executa a ferramenta xpdf conforme o sistema operacional
    if sist_op == 'Linux':
        subprocess.run(['pdftotext', path+"\\"+filename, target_text_path ], capture_output = True)
    elif sist_op == 'Windows':
        subprocess.run(['pdftotext', path+"\\"+filename, target_text_path ], capture_output = True)
    else:
        print("Sistema operacional não reconhecido")
        exit()

    st.write("Arquivo convertido com sucesso!")

    # Criando o botão de download
    #with open(r""+filename.replace(".pdf",".txt"), "a" ,encoding="utf-16", errors='ignore') as f:
    #    st.download_button(f'Download {filename.replace(".pdf",".txt")}', f, file_name=filename.replace(".pdf",".txt"))

#filename = "files\\pdf\\BO_203-2022.pdf"
#target_text_filename = "BO_203-2022.txt"
#target_text_path = os.path.join("files\\txt",target_text_filename)
#subprocess.run(['tools\win64\pdftotext.exe', filename, target_text_path ], capture_output = True)

# Ler o arquivo pdf
def load_file():
    # Preparando para receber um documento no formato PDF
    document = st.file_uploader("", type=["pdf"])

    # Executa uma instrução if assim que um documento for selectionado
    if document is not None:

        # Botão para converter o arquivo PDF
        btnConv = st.button('Converter para TXT')
        
        # Converte o arquivo para TXT após o usuário clicar no botão
        if btnConv:

            # Armazenando no diretório o arquivo a ser convertido
            with open(document.name,"wb") as f:
                f.write(document.getbuffer())

            # movendo o arquivo para a pasta files/pdf
            #shutil.move(document.name, "files\\pdf")
            shutil.move(document.name, PDF_FOLDER)

            # Convertendo para o formato txt
            # conv_file("files\\pdf\\"+document.name, platform.system())
            conv_file(PDF_FOLDER, document.name, platform.system())

def main():
    st.title('PDF CONVERTER')
    st.subheader('')
    st.subheader('Conversor pdf para o formato txt')
    st.subheader('')
    st.text('Arraste um arquivo pdf para realizar a conversão')
    load_file()

if __name__ == "__main__":
    main()
    
