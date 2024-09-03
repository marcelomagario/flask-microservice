# Use uma imagem base oficial do Python
FROM python:3.8-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .

# Defina a variável de ambiente para não gerar arquivos pyc
ENV PYTHONUNBUFFERED=1

# Comando para rodar a aplicação Flask
CMD ["python", "app.py"]
