import pandas as pd
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Carregar variáveis de ambiente
load_dotenv()

# Caminho do arquivo CSV
file_path = './data/data_science_job.csv'

# Verifica se o arquivo CSV existe
if os.path.exists(file_path):
    # Carrega o dataset
    data = pd.read_csv(file_path)

    # Dicionários de mapeamento
    experience_mapping = {
        'EN': 'Entry-level',
        'MI': 'Mid-level',
        'SE': 'Senior-level',
        'EX': 'Expert-level'
    }

    employment_type_mapping = {
        'FT': 'Full-time',
        'PT': 'Part-time',
        'CT': 'Contract',
        'FL': 'Freelance'
    }

    # 1. Limpeza dos Dados
    data = data.dropna()  # Remove registros com valores zerados
    data = data[data['salary'] > 0]  

    # Remove espaços e valores que possam confundir a analise
    data['experience_level'] = data['experience_level'].str.strip().map(experience_mapping)
    data['employment_type'] = data['employment_type'].str.strip().map(employment_type_mapping)
    data['work_setting'] = data['work_setting'].str.strip().str.capitalize()

    # Salva dados limpos em Parquet
    cleaned_file_path = './data/cleaned_data_science_job.parquet'
    data.to_parquet(cleaned_file_path, index=False)
    print("Dados limpos e salvos no arquivo 'cleaned_data_science_job.parquet'.")

    # Conecta ao MongoDB
    MONGODB_URL = os.getenv('MONGODB_URL')
    if MONGODB_URL:
        client = MongoClient(MONGODB_URL)
        db = client['DataAnalisys']
        collection = db['ParqueFiles']

        # Utiliza o pandas pra ler o arquivo parquet salvo acima
        data = pd.read_parquet(cleaned_file_path)

        # Converter DataFrame para JSON-like
        data_dict = data.to_dict("records")

        # Inserir dados no MongoDB
        try:
            collection.insert_many(data_dict)
            print("Dados do arquivo Parquet inseridos no MongoDB com sucesso!")
        except Exception as e:
            print("Erro ao inserir os dados no MongoDB:", e)
    else:
        print("A variável de ambiente MONGODB_URL não está definida.")
else:
    print(f"O arquivo '{file_path}' não foi encontrado.")
