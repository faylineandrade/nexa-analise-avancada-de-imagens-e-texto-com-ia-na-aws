# Projeto de Reconhecimento de Celebridades com AWS Rekognition

Este projeto usa a **AWS Rekognition** para detectar celebridades em imagens e desenhar caixas ao redor dos rostos detectados, além de exibir os nomes das celebridades na imagem. Ele utiliza a biblioteca **boto3** para interagir com a API da AWS e a **Pillow** para manipulação das imagens.
Fruto da parceria entre a DIO e a AWS, denominado: "Nexa: Análise Avançada de Imagens e Texto com IA na AWS".
Iniciado e idealizado pelo especialista Guilherme Carvalho.

## Funcionalidade

- Reconhece celebridades em imagens através do AWS Rekognition.
- Desenha caixas vermelhas ao redor dos rostos detectados.
- Exibe os nomes das celebridades nas imagens.
- Salva as imagens processadas em um novo arquivo com o sufixo `-resultado.jpg`.

## Pré-requisitos

Antes de executar o projeto, você precisa:

1. **Credenciais da AWS**: Certifique-se de que suas credenciais da AWS estão configuradas corretamente. Você pode configurá-las com o comando:
   ```bash
   aws configure
   ```
   Isso irá pedir a sua chave de acesso e chave secreta da AWS.

2. **Dependências do projeto**: Instale as dependências necessárias. Você pode fazer isso com o comando:
   ```bash
   pip install boto3 pillow mypy-boto3-rekognition
   ```

## Como Usar

1. **Coloque suas imagens**: Coloque as imagens que você deseja processar na pasta `images`. O projeto já está configurado para processar as seguintes imagens:

   - `beyonce.jpg`
   - `rihanna.jpg`
   - `ladygaga.jpg`
   - `beyonce_rihanna.jpg`
   - `beyonce_ladygaga.jpg`
   - 
2. **Execute o script**: Após colocar suas imagens na pasta `images`, execute o script `main.py`:
   ```bash
   python main.py
   ```

3. **Resultado**: As imagens processadas serão salvas com o sufixo `-resultado.jpg` no nome do arquivo original, com as caixas e os nomes das celebridades adicionados.

   Exemplo de nome de arquivo de saída:
   - `beyonce-resultado.jpg`
   - `rihanna-resultado.jpg`
   - `beyonce_rihanna-resultado.jpg`

## Considerações

- O código foi feito para funcionar com imagens contendo rostos de celebridades como Beyoncé, Rihanna e Lady Gaga, mas pode ser adaptado para outros casos.
- A detecção é feita com uma confiança mínima de 90%. Se o AWS Rekognition detectar as celebridades com menos de 90% de confiança, a caixa não será desenhada.

