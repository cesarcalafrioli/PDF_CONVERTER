import streamlit as st
import platform
import subprocess
import os
import shutil

# Cria os diretórios onde ficarão os arquivos caso ainda não existam
if not os.path.exists('files'):
    os.makedirs('files/pdf')
    os.makedirs('files/txt') 

# Diretórios onde ficarão armazenados os arquivos PDF e TXT conforme seu sistema operacional
if platform.system() == "Linux":
    PDF_FOLDER = "files//pdf"
    TXT_FOLDER = "files//txt"
elif platform.system() == "Windows":
    PDF_FOLDER = "files\\pdf"
    TXT_FOLDER = "files\\txt"
else:
    print("Sistema operacional não reconhecido")
    exit()


# Converte o arquivo pdf para o formato txt.
# Detecta em qual sistema operacional o script está rodando
def conv_file(path, filename, sist_op):

    # Informa onde vai ficar o arquivo txt
    dir_arq_conv = os.path.join(TXT_FOLDER, filename.replace(".pdf",".txt"))

    # Executa a ferramenta xpdf conforme o sistema operacional
    # pdftotext <arquivo pdf> <diretorio e o nome do arquivo a ser convertido>
    if sist_op == 'Linux':
        if subprocess.run(['pdftotext', path+"//"+filename, dir_arq_conv ], capture_output = True):
            os.remove(path+"//"+filename)
    elif sist_op == 'Windows':
        if subprocess.run(['pdftotext', path+"\\"+filename, dir_arq_conv ], capture_output = True):
            os.remove(path+"\\"+filename)
    else:
        print("Sistema operacional não reconhecido")
        exit()

    st.write("Arquivo convertido com sucesso!")

    # Criando o botão de download
    with open(r""+dir_arq_conv , encoding="utf-8" , errors='ignore') as f:
        st.download_button(f'Baixar o arquivo', f, filename.replace(".pdf",".txt"))

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
            shutil.move(document.name, PDF_FOLDER)

            # Convertendo para o formato txt
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
    
