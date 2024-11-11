import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a URL de conexão do MongoDB
MONGODB_URL = os.getenv('MONGODB_URL')
client = MongoClient(MONGODB_URL)

# Selecionar o banco de dados e a coleção
db = client['DataAnalisys']
collection = db['ParqueFiles']

# Caminho para o arquivo Parquet
file_path = './data/cleaned_data_science_job.parquet'

# Carregar o arquivo Parquet usando pandas
data = pd.read_parquet(file_path)

# Converter o DataFrame para uma lista de dicionários (JSON-like)
data_dict = data.to_dict("records")

# Inserir todos os registros no MongoDB
try:
    collection.insert_many(data_dict)
    print("Dados do arquivo Parquet inseridos no MongoDB com sucesso!")
except Exception as e:
    print("Erro ao inserir os dados:", e)
