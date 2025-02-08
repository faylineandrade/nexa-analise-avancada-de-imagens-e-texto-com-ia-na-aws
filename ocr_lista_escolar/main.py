import json
from pathlib import Path
import boto3
from botocore.exceptions import ClientError


def detect_file_text() -> None:

    client = boto3.client("textract")
    

    file_path = str(Path(__file__).parent / "images" / "lista-material-escolar.jpeg")
    with open(file_path, "rb") as f:
        document_bytes = f.read()

    try:
        response = client.detect_document_text(Document={"Bytes": document_bytes})

        with open("response.json", "w") as response_file:
            response_file.write(json.dumps(response, indent=4))
    except ClientError as e:
        print(f"Erro ao processar o documento: {e}")


def get_lines() -> list[str]:
   
    try:
        with open("response.json", "r") as f:
            data = json.loads(f.read())
            blocks = data["Blocks"]

        return [block["Text"] for block in blocks if block["BlockType"] == "LINE"]
    except FileNotFoundError:
        print("Arquivo response.json não encontrado. Processando a imagem!")
        detect_file_text()
        return get_lines()
    except Exception as e:
        print(f"Erro ao ler as linhas: {e}")
        return []


if __name__ == "__main__":
    for line in get_lines():
        print(line)
