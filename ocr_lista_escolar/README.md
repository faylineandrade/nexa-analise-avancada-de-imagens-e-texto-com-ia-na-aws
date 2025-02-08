# OCR Lista Escolar

Este projeto é fruto da parceria entre a DIO e a AWS, denominado: "Nexa: Análise Avançada de Imagens e Texto com IA na AWS". O objetivo é demonstrar a aplicação do AWS Textract para OCR (Reconhecimento Óptico de Caracteres), extraindo automaticamente texto de uma imagem de lista de materiais escolares.
Iniciada e idealizada pelo especialista Guilherme Carvalho.

##  Pré-requisitos

Certifique-se de ter:
- Python 3.9 ou superior instalado.
- Ferramenta [UV](https://uvicorn.org/) instalada para gerenciar dependências.
- Conta na AWS com permissões configuradas para o serviço Textract.

## Etapas do Projeto
- Upload da Imagem – A lista de materiais foi carregada no AWS S3.
- Processamento com Textract – Extração automática do texto contido na imagem.
- Análise dos Resultados – Verificação da precisão e insights sobre o uso do Textract.

## Insights e Aprendizados
- AWS Textract é uma solução poderosa para automação de OCR.
- Imagens de boa qualidade melhoram significativamente a precisão da extração.
- O processamento pode ser combinado com outras ferramentas, como NLP, para enriquecer a análise.


## Configuração do Ambiente

1. Configure suas credenciais da AWS:
   ```
   aws configure
   ```
2. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/ocr-lista-escolar.git
   cd ocr-lista-escolar
   ```
3. Instale as dependências:
   ```
   uv install
   ```

## Execução

Para executar o projeto, use o comando:
```
uv run main.py
```

O script processará a imagem localizada em `images/lista-material-escolar.jpeg`, salvará a resposta em `response.json` e exibirá no terminal as linhas extraídas.

## Exemplo de Imagem

Abaixo está a imagem utilizada como exemplo no projeto:

![Lista Material Escolar](images/lista-material-escolar.jpeg)

## Estrutura do Projeto

- `main.py`: Script principal que contém as funções para processar a imagem e extrair texto.
- `pyproject.toml`: Arquivo de configuração das dependências do projeto.
- `uv.lock`: Arquivo gerado automaticamente pelo gerenciador UV.
- `response.json`: Resposta do AWS Textract com os dados extraídos da imagem.
- `images/`: Diretório que contém a imagem utilizada no exemplo.

##  Insights e Aprendizados

Durante a construção deste projeto, foram explorados:
- A integração com o serviço AWS Textract para análise de documentos.
- O uso do Python e da biblioteca Boto3 para interagir com serviços da AWS.
- A importância da modularização e documentação em projetos técnicos.

## Possibilidades Futuras

Este projeto pode ser expandido para incluir:
- Suporte à análise de formulários ou tabelas utilizando a função `analyze_document` do Textract.
- Processamento em lote de múltiplas imagens armazenadas no Amazon S3.
- Implementação de uma interface gráfica para facilitar o envio e processamento das imagens.
