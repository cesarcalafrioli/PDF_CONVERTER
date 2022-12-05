## CONVERSOR DE PDF

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![License](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)](https://shields.io/)
[![License](https://img.shields.io/github/license/cesarcalafrioli/PDF_CONVERTER)](https://shields.io/)
[![License](https://img.shields.io/github/issues/cesarcalafrioli/PDF_CONVERTER)](https://shields.io/)
[![License](https://img.shields.io/github/forks/cesarcalafrioli/PDF_CONVERTER)](https://shields.io/)
[![License](https://img.shields.io/github/stars/cesarcalafrioli/PDF_CONVERTER)](https://shields.io/)

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Como funciona](#como-funciona)
* [Instruções](#instrucoes)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Licença](#licença)

## Descrição do Projeto

PDF Converter é um aplicativo web criado para facilitar a conversão de um arquivo PDF para o formato TXT e, em seguida, gerar a opção de download. O aplicativo utiliza a ferramenta xpdf, um projeto opensource que inclui, além do visualizador pdf, um conjunto de ferramendas usadas via prompt de comando voltadas para manipulação de arquivos pdf.

Mais informações sobre o xpdf acesse o site http://www.xpdfreader.com

## Como funciona

O aplicativo recebe o arquivo PDF enviado pelo usuário. Após este clicar no botão de converter,o arquivo enviado é colocado temporariamente em uma subpasta chamada pdf localizada na pasta files e, em seguida, realiza a sua conversão para o formato txt. O arquivo convertido é colocado na subpasta txt, que também fica na pasta files, enquanto o arquivo PDF é apagado.

## Instruções

1. Instale as ferramentas de linha de comando xpdf conforme o seu sistema operacional.

    **Instalando no linux**

    ```
    wget --no-check-certificate https://dl.xpdfreader.com/xpdf-tools-linux-4.04.tar.gz
    tar -xvf xpdf-tools-linux-4.04.tar.gz && sudo cp xpdf-tools-linux-4.04/bin64/pdftotext /usr/local/bin
    ```

    **Instalando no windows**

    1 - Execute os comandos abaixo no powershell
    ```
    Invoke-WebRequest https://dl.xpdfreader.com/xpdf-tools-win-4.04.zip -OutFile $env:userprofile\Downloads\xpdf-tools-win-4.04.zip
    Expand-Archive -Path $env:userprofile\Downloads\xpdf-tools-win-4.04.zip -DestinationPath C:\
    ```

    2 - Em Painel de controle > Sistemas > Configurações avançadas do sistemas > Variáveis de ambiente, adicione na variável Path o diretório ```C:\xpdf-tools-win-4.04             \bin64```, e clique em Ok.


2. É necessário rodar esse aplicativo em um ambiente virtual python. Veja este [tutorial](https://github.com/cesarcalafrioli/tutorial-ambiente-virtual-python) para saber como.
3. Instale os pacotes listados acima.
```
pip install -r requirements.txt
```
4. Rode o streamlit
```
streamlit run app.py
```

O script irá abrir a ferramenta no navegador web.


## Tecnologias utilizadas

- python versão 3
- xpdf ( É necessário instalar o xpdf separadamente, bem como configurar o ambiente de execução para que o aplicativo execute o comando da ferrammenta ).
- streamlit


## Licença

Licença MIT - César Augusto de Carvalho Calafrioli Móes
