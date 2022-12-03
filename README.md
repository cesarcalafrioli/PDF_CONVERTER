## CONVERSOR DE PDF

EM DESENVOLVIMENTO

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![License](https://img.shields.io/github/license/cesarcalafrioli/PDF_CONVERTER)](https://shields.io/)
[![License](https://img.shields.io/github/issues/cesarcalafrioli/PDF_CONVERTER)](https://shields.io/)
[![License](https://img.shields.io/github/forks/cesarcalafrioli/PDF_CONVERTER)](https://shields.io/)
[![License](https://img.shields.io/github/stars/cesarcalafrioli/PDF_CONVERTER)](https://shields.io/)

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Licença](#licença)

## Descrição do Projeto

PDF Converter é um aplicativo web criado para facilitar a conversão de um arquivo PDF para o formato TXT e, em seguida, gerar a opção de download. O aplicativo utiliza a ferramenta xpdf, um projeto opensource que inclui, além do visualizador pdf, um conjunto de ferramendas usadas via prompt de comando voltadas para manipulação de arquivos pdf.

Mais informações sobre o xpdf acesse o site http://www.xpdfreader.com

## Status do projeto

Em desenvolvimento.

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
Invoke-WebRequest https://dl.xpdfreader.com/xpdf-tools-win-4.04.zip -OutFile C:\Users\$USERNAME\Downloads\xpdf-tools-win-4.04.zip
Expand-Archive -Path C:\Users\%username%\Downloads\xpdf-tools-win-4.04.zip -DestinationPath C:\
```
2 - Em Painel de controle > Sistemas > Configurações avançadas do sistemas > Variáveis de ambiente, adicione na variável Path o diretório ```C:\xpdf-tools-win-4.04\bin64```, e clique em Ok.


2. É necessário rodar esse aplicativo em um ambiente virtual python. Veja este [tutorial](https://github.com/cesarcalafrioli/tutorial-ambiente-virtual-python) para saber como.
3. Instale os pacotes listados acima.
```
pip install -r requirements.txt
```
4. Rode o streamlit
```
streamlit run boletins_servico.py
```

O script irá abrir a ferramenta no navegador web.
.

## Funcionalidades e Demonstração da Aplicação



## Tecnologias utilizadas

- python versão 3
- xpdf ( É necessário instalar o xpdf separadamente, bem como configurar o ambiente de execução para que o aplicativo execute o comando da ferrammenta ).
- streamlit


## Licença

Licença MIT - César Augusto de Carvalho Calafrioli Móes
